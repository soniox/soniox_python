import numpy
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
