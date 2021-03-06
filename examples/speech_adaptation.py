import os
from soniox.transcribe_file import transcribe_file_short
from soniox.speech_service import Client, SpeechContext, SpeechContextEntry, set_api_key

THIS_DIR = os.path.join(os.path.realpath(os.path.dirname(__file__)))

set_api_key("<YOUR-API-KEY>")


def test(client: Client, audio_file: str, speech_context: SpeechContext) -> None:
    base_result = transcribe_file_short(audio_file, client)
    base_text = " ".join(w.text for w in base_result.words)

    adapted_result = transcribe_file_short(audio_file, client, speech_context=speech_context)
    adapted_text = " ".join(w.text for w in adapted_result.words)

    print(f"{audio_file}")
    print(f"  Base transcript: {base_text}")
    print(f"  With adaptation: {adapted_text}")
    print()


def main():
    with Client() as client:
        test(
            client,
            os.path.join(THIS_DIR, "test_audio_speech_adaptation_1.flac"),
            SpeechContext(entries=[SpeechContextEntry(phrases=["see is"], boost=10.0,),]),
        )


if __name__ == "__main__":
    main()
