from soniox.transcribe_file import transcribe_file_short
from soniox.speech_service import Client, set_api_key
from soniox.test_data import TEST_AUDIO_PROFANITY_MP3

set_api_key("<YOUR-API-KEY>")


def main():
    with Client() as client:
        result = transcribe_file_short(
            TEST_AUDIO_PROFANITY_MP3,
            client,
            enable_profanity_filter=True,
        )
        print("Words: " + " ".join(w.text for w in result.words))


if __name__ == "__main__":
    main()
