from typing import Iterable
from soniox.transcribe_live import transcribe_stream
from soniox.speech_service import Client, set_api_key
from soniox.test_data import TEST_AUDIO_LONG_FLAC

set_api_key("<YOUR-API-KEY>")

def iter_audio() -> Iterable[bytes]:
    with open(TEST_AUDIO_LONG_FLAC, "rb") as fh:
        while True:
            audio = fh.read(1024)
            if len(audio) == 0:
                break
            yield audio

def main():
    with Client() as client:
        for result in transcribe_stream(iter_audio(), client):
            # Variable result contains final and non-final words.
            print(" ".join(w.text for w in result.words))

if __name__ == "__main__":
    main()