from soniox.transcribe_live import transcribe_microphone
from soniox.speech_service import Client, set_api_key

set_api_key("<YOUR-API-KEY>")


def main():
    with Client() as client:
        print("Transcribing from your microphone ...")
        for result in transcribe_microphone(client):
            print(" ".join(w.text for w in result.words))


if __name__ == "__main__":
    main()
