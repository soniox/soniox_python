from typing import Optional, List, Dict
from soniox.speech_service import Result, Word

PUNCT_WORDS = [",", ".", "?"]


def get_words_with_speaker(result: Result, speaker: int) -> List[Word]:
    out_words: List[Word] = []
    for word in result.words:
        out_word = Word()
        out_word.CopyFrom(word)
        out_word.speaker = speaker
        out_words.append(out_word)
    return out_words


def build_segments(words: List[Word], silence_threshold_ms: int) -> List[List[Word]]:
    out_segments: List[List[Word]] = []
    last_end_ms: Optional[int] = None

    for word in words:
        not_punct = word.text not in PUNCT_WORDS

        if len(out_segments) == 0 or (
            not_punct
            and last_end_ms is not None
            and word.start_ms - last_end_ms > silence_threshold_ms
        ):
            out_segments.append([word])
        else:
            out_segments[-1].append(word)

        if not_punct:
            last_end_ms = word.start_ms + word.duration_ms

    return out_segments


def get_merged_words(results: Dict[int, Result], silence_threshold_ms: int) -> List[Word]:
    channels = results.keys()

    segments: Dict[int, List[List[Word]]] = {}
    for c in channels:
        speaker = 1 + c
        words = get_words_with_speaker(results[c], speaker)
        segments[c] = build_segments(words, silence_threshold_ms)

    out_words: List[Word] = []
    position: Dict[int, int] = {c: 0 for c in channels}

    while True:
        avail_channels = [c for c in channels if position[c] < len(segments[c])]
        if len(avail_channels) == 0:
            break

        c = min(avail_channels, key=lambda c: segments[c][position[c]][0].start_ms)

        out_words += segments[c][position[c]]
        position[c] += 1

    return out_words


def fix_punctuation(words: List[Word]) -> List[Word]:
    out_words: List[Word] = []

    def fix_end_of_sentence(prev_word: Word) -> None:
        if prev_word.text == ",":
            prev_word.text = "."
        elif prev_word.text in PUNCT_WORDS:
            pass
        else:
            new_word = Word()
            new_word.text = "."
            new_word.start_ms = prev_word.start_ms + prev_word.duration_ms
            new_word.duration_ms = 0
            new_word.is_final = prev_word.is_final
            new_word.speaker = prev_word.speaker
            out_words.append(new_word)

    for word in words:
        if len(out_words) == 0:
            out_words.append(word)
            continue

        prev_word = out_words[-1]
        if word.speaker == prev_word.speaker:
            out_words.append(word)
            continue

        fix_end_of_sentence(prev_word)

        word.text = word.text.capitalize()
        out_words.append(word)

    if len(out_words) > 0:
        fix_end_of_sentence(out_words[-1])

    return out_words


def build_transcript(words: List[Word]) -> str:
    transcript_parts: List[str] = []
    current_speaker: Optional[int] = None

    for word in words:
        if current_speaker is None or word.speaker != current_speaker:
            if current_speaker is not None:
                transcript_parts.append("\n")

            current_speaker = word.speaker
            transcript_parts.append(f"[speaker:{current_speaker}] ")

        if word.text not in PUNCT_WORDS and not transcript_parts[-1].endswith(" "):
            transcript_parts.append(" ")

        transcript_parts.append(word.text)

    if current_speaker is not None:
        transcript_parts.append("\n")

    return "".join(transcript_parts)


def get_multi_channel_transcript(results: Dict[int, Result], silence_threshold_ms: int) -> str:
    merged_words = get_merged_words(results, silence_threshold_ms)
    merged_words = fix_punctuation(merged_words)
    return build_transcript(merged_words)
