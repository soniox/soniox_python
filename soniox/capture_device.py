import numpy
import time
import random
from abc import ABC, abstractmethod


NUM_CHANNELS = 1
SAMPLE_RATE = 16000
PREFERRED_FRAME_SIZE = 1280


class AbstractCaptureDevice(ABC):
    @abstractmethod
    def start(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def stop(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def read_audio(self) -> bytes:
        """
        Must return audio using PCM signed 16-bit little endian encoding,
        16 kHz sample rate, 1 channel.
        """
        raise NotImplementedError()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()


class MicrophoneCaptureDevice(AbstractCaptureDevice):
    def __init__(self) -> None:
        import soundcard

        self._soundcard = soundcard
        self._recorder_ctx = None
        self._recorder = None

    def start(self) -> None:
        if self._recorder_ctx is not None:
            return
        mic = self._soundcard.default_microphone()
        self._recorder_ctx = mic.recorder(
            samplerate=SAMPLE_RATE, channels=NUM_CHANNELS, blocksize=PREFERRED_FRAME_SIZE
        )
        self._recorder = self._recorder_ctx.__enter__()

    def stop(self) -> None:
        if self._recorder_ctx is None:
            return
        self._recorder = None
        self._recorder_ctx.__exit__(None, None, None)
        self._recorder_ctx = None

    def read_audio(self) -> bytes:
        assert self._recorder is not None
        samples = self._recorder.record(numframes=PREFERRED_FRAME_SIZE)
        samples *= 32768
        numpy.clip(samples, -32768, 32767, out=samples)
        samples = numpy.ascontiguousarray(samples, "<h")
        data = samples.tobytes()
        return data


class SimulatedCaptureDevice(AbstractCaptureDevice):
    """This class implements AbstractCaptureDevice by reading raw audio
    samples from a file (encoding must be PCM 16-bit little endian 16 kHz)."""

    def __init__(self, audio_file: str, start_random: bool = False) -> None:
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

        # Set the initial audio position.
        if start_random:
            self._position = random.randrange(num_chunks) * self._chunk_size
        else:
            self._position = 0

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
