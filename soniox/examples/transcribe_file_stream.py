from soniox.transcribe_file import transcribe_file_stream
from soniox.speech_service import Client, set_api_key
from soniox.test_data import TEST_AUDIO_LONG_FLAC

set_api_key("<YOUR-API-KEY>")


def main():
    with Client() as client:
        result = transcribe_file_stream(TEST_AUDIO_LONG_FLAC, client)
        print(" ".join(w.text for w in result.words))


if __name__ == "__main__":
    main()
