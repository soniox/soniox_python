from soniox.transcribe_file import transcribe_file_stream
from soniox.speech_service import Client, set_api_key
from soniox.test_data import TEST_AUDIO_MULTI_CHANNEL_FLAC

set_api_key("<YOUR-API-KEY>")


def main():
    with Client() as client:
        channel_results = transcribe_file_stream(
            TEST_AUDIO_MULTI_CHANNEL_FLAC,
            client,
            num_audio_channels=2,
            enable_separate_recognition_per_channel=True,
        )
        for result in channel_results:
            print(f"Channel {result.channel}: " + " ".join(word.text for word in result.words))


if __name__ == "__main__":
    main()
