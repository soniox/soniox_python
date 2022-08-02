from soniox.transcribe_file import transcribe_file_short
from soniox.speech_service import Client, set_api_key
from soniox.test_data import TEST_AUDIO_FLAC

set_api_key("<YOUR-API-KEY>")


def main():
    with Client() as client:
        # By specifying profanity_filter_phrases, the these phrases will
        # be considered profane, in addition to the default logic.
        result = transcribe_file_short(
            TEST_AUDIO_FLAC,
            client,
            enable_profanity_filter=True,
            profanity_filter_phrases=["two years", "homesick"],
        )
        for word in result.words:
            print(f"{word.text} {word.start_ms} {word.duration_ms}")


if __name__ == "__main__":
    main()
