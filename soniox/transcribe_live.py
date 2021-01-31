from typing import Iterable, Optional
import threading
from soniox.capture_device import (
    AbstractCaptureDevice,
    MicrophoneCaptureDevice,
    NUM_CHANNELS,
    SAMPLE_RATE,
)
from soniox.speech_service import (
    Client,
    TranscribeStreamConfig,
    Result,
    SpeechContext,
)


def transcribe_capture(
    capture_device: AbstractCaptureDevice,
    client: Client,
    include_nonfinal: bool = True,
    speech_context: Optional[SpeechContext] = None,
    stop_event: Optional[threading.Event] = None,
) -> Iterable[Result]:
    assert isinstance(capture_device, AbstractCaptureDevice)
    assert isinstance(client, Client)
    assert isinstance(include_nonfinal, bool)
    assert speech_context is None or isinstance(speech_context, SpeechContext)

    config = TranscribeStreamConfig()
    config.audio_format = "pcm_s16le"
    config.sample_rate_hertz = SAMPLE_RATE
    config.num_audio_channels = NUM_CHANNELS
    config.include_nonfinal = include_nonfinal
    if speech_context is not None:
        config.speech_context.CopyFrom(speech_context)

    if stop_event is None:
        stop_event = threading.Event()

    with capture_device:

        def iter_audio() -> Iterable[bytes]:
            while True:
                audio = capture_device.read_audio()
                if stop_event.is_set():
                    break
                yield audio

        yield from client.TranscribeStream(config, iter_audio())


def transcribe_microphone(
    client: Client,
    include_nonfinal: bool = True,
    speech_context: Optional[SpeechContext] = None,
    stop_event: Optional[threading.Event] = None,
):
    return transcribe_capture(
        MicrophoneCaptureDevice(), client, include_nonfinal, speech_context, stop_event
    )


def transcribe_stream(
    iter_audio: Iterable[bytes],
    client: Client,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
) -> Iterable[Result]:
    assert isinstance(client, Client)
    assert isinstance(sample_rate_hertz, int)
    assert isinstance(num_audio_channels, int)
    assert speech_context is None or isinstance(speech_context, SpeechContext)

    config = TranscribeStreamConfig()
    config.audio_format = audio_format
    config.sample_rate_hertz = sample_rate_hertz
    config.num_audio_channels = num_audio_channels
    config.include_nonfinal = True
    if speech_context is not None:
        config.speech_context.CopyFrom(speech_context)

    yield from client.TranscribeStream(config, iter_audio)
