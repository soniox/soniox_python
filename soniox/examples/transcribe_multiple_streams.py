import threading
from typing import Iterable
from soniox.transcribe_live import transcribe_stream
from soniox.speech_service import Client, set_api_key
from soniox.test_data import TEST_AUDIO_LONG_RAW

set_api_key("<YOUR-API-KEY>")

# Number of channels we transcribe in parallel.
NUM_CHANNELS = 4


class Channel:
    def __init__(self, idx: int, client: Client) -> None:
        self._idx = idx
        self._client = client

    def iter_audio(self) -> Iterable[bytes]:
        with open(TEST_AUDIO_LONG_RAW, "rb") as fh:
            while True:
                audio = fh.read(1024)
                if len(audio) == 0:
                    break
                yield audio

    def run(self) -> None:
        for result in transcribe_stream(
            self.iter_audio(),
            self._client,
            audio_format="pcm_s16le",
            sample_rate_hertz=16000,
            num_audio_channels=1,
        ):
            words = " ".join([w.text for w in result.words])
            print(f"Channel {self._idx}: {words}")


def main():
    # Create a single client for all channels / threads.
    with Client() as client:
        # Create channels and start threads that run Channel.run().
        threads = []
        for channel_num in range(NUM_CHANNELS):
            channel = Channel(channel_num, client)
            thread = threading.Thread(target=channel.run)
            thread.start()
            threads.append(thread)

        # Join threads.
        for thread in threads:
            thread.join()


if __name__ == "__main__":
    main()
