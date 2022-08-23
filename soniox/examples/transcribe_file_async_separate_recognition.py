import time
from soniox.speech_service import Client, set_api_key
from soniox.transcribe_file import transcribe_file_async
from soniox.test_data import TEST_AUDIO_MULTI_CHANNEL_FLAC

set_api_key("<YOUR-API-KEY>")


def main():
    with Client() as client:
        print("Uploading file.")
        file_id = transcribe_file_async(
            TEST_AUDIO_MULTI_CHANNEL_FLAC,
            client,
            num_audio_channels=2,
            enable_separate_recognition_per_channel=True,
            transcribe_async_mode="instant_file",
            reference_name="test",
        )
        print(f"File ID: {file_id}")

        while True:
            print("Calling GetTranscribeAsyncFileStatus.")
            status = client.GetTranscribeAsyncFileStatus(file_id)
            print(f"Status: {status.status}")
            if status.status in ("COMPLETED", "FAILED"):
                break
            time.sleep(2.0)

        if status.status == "COMPLETED":
            print("Calling GetTranscribeAsyncResult")
            channel_results = client.GetTranscribeAsyncResult(file_id)
            for result in channel_results:
                print(f"Channel {result.channel}: " + " ".join(word.text for word in result.words))
        else:
            print(f"Transcription failed with error: {status.error_message}")

        print("Calling DeleteTranscribeAsyncFile.")
        client.DeleteTranscribeAsyncFile(file_id)


if __name__ == "__main__":
    main()
