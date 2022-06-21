import threading
import time
import signal
import random
from soniox.capture_device import AbstractCaptureDevice, SAMPLE_RATE, PREFERRED_FRAME_SIZE
from soniox.transcribe_live import transcribe_capture
from soniox.speech_service import Client
from soniox.test_data import TEST_AUDIO_RAW

# Number of channels we transcribe in parallel.
NUM_CHANNELS = 8

# Lock to prevent overlapping printouts.
print_lock = threading.Lock()


# This class implements AbstractCaptureDevice by reading raw audio samples
# from a file (encoding must be PCM 16-bit little endian 16 kHz).
class SimulatedCaptureDevice(AbstractCaptureDevice):
    def __init__(self, audio_file: str) -> None:
        # Read the audio file.
        with open(audio_file, "rb") as fh:
            self._audio = fh.read()

        # Calculate the chunk size in bytes.
        # Multiply by 2 because the files use 16-bit encoding.
        self._chunk_size = 2 * PREFERRED_FRAME_SIZE

        # Calculate the number of chunks in the audio.
        num_chunks = len(self._audio) // self._chunk_size
        if num_chunks == 0:
            raise Exception(f"File {audio_file} does not have enough audio for one chunk.")

        # Calculate the time delay between chunks to simulate real-time audio.
        self._delay_sec = PREFERRED_FRAME_SIZE / SAMPLE_RATE

        # Set the initial audio position randomly.
        self._position = random.randrange(num_chunks) * self._chunk_size

        # Set the initial time.
        self._time = time.monotonic()

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def read_audio(self) -> bytes:
        # Delay to simulate real-time audio.
        now = time.monotonic()
        delay = self._time + self._delay_sec - now
        if delay > 0.0:
            time.sleep(delay)
        self._time = time.monotonic()

        # If there is not enough audio left for one chunk, reset the
        # position to the beginning.
        if len(self._audio) - self._position < self._chunk_size:
            self._position = 0
        # Get one chunk of audio.
        audio_chunk = self._audio[self._position : self._position + self._chunk_size]
        # Increment the audio position.
        self._position += self._chunk_size
        # Return the chunk.
        return audio_chunk


class Channel:
    def __init__(self, channel_num: int, client: Client, stop_event: threading.Event) -> None:
        self._channel_num = channel_num
        self._client = client
        self._stop_event = stop_event

        # Create a SimulatedCaptureDevice.
        self._capture_device = SimulatedCaptureDevice(TEST_AUDIO_RAW)

    def run(self) -> None:
        # Call transcribe_capture with our capture device to transcribe.
        # We specify include_nonfinal=True (the default) to request nonfinal
        # words. If they are not desired, specify False. For example this
        # could be done if the stream was going to be time delayed and
        # annotated with captions based only on final words.
        for result in transcribe_capture(
            self._capture_device, self._client, include_nonfinal=True, stop_event=self._stop_event
        ):
            # Print words.
            final_str = " ".join(w.text for w in result.words if w.is_final)
            nonfinal_str = " ".join(w.text for w in result.words if not w.is_final)
            with print_lock:
                print(f"Channel {self._channel_num}:")
                print(f"  Final: {final_str}")
                print(f"  Nonfinal: {nonfinal_str}")


def main():
    # Set up a threading.Event which will be set when CTRL+C is pressed.
    stop_event = threading.Event()

    def sigint_handler(sig, stack):
        print("Interrupted, finishing...")
        stop_event.set()

    signal.signal(signal.SIGINT, sigint_handler)

    # Create a client to use for all transcriptions.
    with Client() as client:
        # Create channels and start threads that run Channel.run.
        threads = []
        for channel_num in range(NUM_CHANNELS):
            channel = Channel(channel_num, client, stop_event)
            thread = threading.Thread(target=channel.run)
            thread.start()
            threads.append(thread)

        # Join the threads, which will finish soon after stop_event is set.
        for thread in threads:
            thread.join()


if __name__ == "__main__":
    main()

