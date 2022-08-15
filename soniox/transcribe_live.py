from typing import Iterable, Optional, List
import threading
from soniox.capture_device import (
    AbstractCaptureDevice,
    MicrophoneCaptureDevice,
    NUM_CHANNELS,
    SAMPLE_RATE,
)
from soniox.speech_service import (
    Client,
    TranscriptionConfig,
    Result,
    SpeechContext,
)


def transcribe_capture(
    capture_device: AbstractCaptureDevice,
    client: Client,
    include_nonfinal: bool = True,
    speech_context: Optional[SpeechContext] = None,
    stop_event: Optional[threading.Event] = None,
    enable_profanity_filter: bool = False,
    content_moderation_phrases: Optional[List[str]] = None,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
    model: str = "",
) -> Iterable[Result]:
    assert isinstance(capture_device, AbstractCaptureDevice)
    assert isinstance(client, Client)
    assert isinstance(include_nonfinal, bool)
    assert speech_context is None or isinstance(speech_context, SpeechContext)
    assert isinstance(enable_profanity_filter, bool)
    if content_moderation_phrases is not None:
        assert isinstance(content_moderation_phrases, list)
        assert all(isinstance(phrase, str) for phrase in content_moderation_phrases)
    assert isinstance(enable_streaming_speaker_diarization, bool)
    assert isinstance(enable_global_speaker_diarization, bool)
    assert isinstance(min_num_speakers, int)
    assert isinstance(max_num_speakers, int)
    assert isinstance(enable_speaker_identification, bool)
    if cand_speaker_names is not None:
        assert isinstance(cand_speaker_names, list)
        assert all(isinstance(name, str) for name in cand_speaker_names)
    assert isinstance(model, str)

    config = TranscriptionConfig()
    config.audio_format = "pcm_s16le"
    config.sample_rate_hertz = SAMPLE_RATE
    config.num_audio_channels = NUM_CHANNELS
    config.include_nonfinal = include_nonfinal
    if speech_context is not None:
        config.speech_context.CopyFrom(speech_context)
    config.enable_profanity_filter = enable_profanity_filter
    if content_moderation_phrases is not None:
        config.content_moderation_phrases.extend(content_moderation_phrases)
    config.enable_streaming_speaker_diarization = enable_streaming_speaker_diarization
    config.enable_global_speaker_diarization = enable_global_speaker_diarization
    config.min_num_speakers = min_num_speakers
    config.max_num_speakers = max_num_speakers
    config.enable_speaker_identification = enable_speaker_identification
    if cand_speaker_names is not None:
        config.cand_speaker_names.extend(cand_speaker_names)
    config.model = model

    if stop_event is None:
        stop_event = threading.Event()

    with capture_device:

        def iter_audio() -> Iterable[bytes]:
            while True:
                audio = capture_device.read_audio()
                if stop_event.is_set():
                    break
                yield audio

        yield from client.TranscribeStream(config, iter_audio())


def transcribe_microphone(
    client: Client,
    include_nonfinal: bool = True,
    speech_context: Optional[SpeechContext] = None,
    stop_event: Optional[threading.Event] = None,
    enable_profanity_filter: bool = False,
    content_moderation_phrases: Optional[List[str]] = None,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
    model: str = "",
):
    return transcribe_capture(
        MicrophoneCaptureDevice(),
        client,
        include_nonfinal,
        speech_context,
        stop_event,
        enable_profanity_filter,
        content_moderation_phrases,
        enable_streaming_speaker_diarization,
        enable_global_speaker_diarization,
        min_num_speakers,
        max_num_speakers,
        enable_speaker_identification,
        cand_speaker_names,
        model,
    )


def transcribe_stream(
    iter_audio: Iterable[bytes],
    client: Client,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
    enable_profanity_filter: bool = False,
    content_moderation_phrases: Optional[List[str]] = None,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
    enable_separate_recognition_per_channel: bool = False,
    model: str = "",
) -> Iterable[Result]:
    assert isinstance(client, Client)
    assert isinstance(sample_rate_hertz, int)
    assert isinstance(num_audio_channels, int)
    assert speech_context is None or isinstance(speech_context, SpeechContext)
    assert isinstance(enable_profanity_filter, bool)
    if content_moderation_phrases is not None:
        assert isinstance(content_moderation_phrases, list)
        assert all(isinstance(phrase, str) for phrase in content_moderation_phrases)
    assert isinstance(enable_streaming_speaker_diarization, bool)
    assert isinstance(enable_global_speaker_diarization, bool)
    assert isinstance(min_num_speakers, int)
    assert isinstance(max_num_speakers, int)
    assert isinstance(enable_speaker_identification, bool)
    if cand_speaker_names is not None:
        assert isinstance(cand_speaker_names, list)
        assert all(isinstance(name, str) for name in cand_speaker_names)
    assert isinstance(enable_separate_recognition_per_channel, bool)
    assert isinstance(model, str)

    config = TranscriptionConfig()
    config.audio_format = audio_format
    config.sample_rate_hertz = sample_rate_hertz
    config.num_audio_channels = num_audio_channels
    config.include_nonfinal = True
    if speech_context is not None:
        config.speech_context.CopyFrom(speech_context)
    config.enable_profanity_filter = enable_profanity_filter
    if content_moderation_phrases is not None:
        config.content_moderation_phrases.extend(content_moderation_phrases)
    config.enable_streaming_speaker_diarization = enable_streaming_speaker_diarization
    config.enable_global_speaker_diarization = enable_global_speaker_diarization
    config.min_num_speakers = min_num_speakers
    config.max_num_speakers = max_num_speakers
    config.enable_speaker_identification = enable_speaker_identification
    if cand_speaker_names is not None:
        config.cand_speaker_names.extend(cand_speaker_names)
    config.enable_separate_recognition_per_channel = enable_separate_recognition_per_channel
    config.model = model

    yield from client.TranscribeStream(config, iter_audio)
