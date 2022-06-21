import time
from soniox.speech_service import Client, set_api_key
from soniox.test_data import TEST_AUDIO_LONG_FLAC

set_api_key("<YOUR-API-KEY>")


def main():
    with Client() as client:
        with open(TEST_AUDIO_LONG_FLAC, "rb") as fh:
            def audio_generator():
                while True:
                    audio = fh.read(32768)
                    if len(audio) == 0:
                        break
                    yield audio

            print("Calling TranscribeAsync.")
            reference_name = "test"
            file_id = client.TranscribeAsync(reference_name, audio_generator())
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
                result = client.GetTranscribeAsyncResult(file_id)
                print("Words: " + " ".join(w.text for w in result.words))

            print("Calling DeleteTranscribeAsyncFile.")
            client.DeleteTranscribeAsyncFile(file_id)


if __name__ == "__main__":
    main()
