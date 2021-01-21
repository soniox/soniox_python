import os
from typing import Optional, Iterable
from soniox.speech_service import (
    Client,
    Result,
    TranscribeConfig,
    TranscribeStreamConfig,
    SpeechContext,
)

READ_CHUNK_SIZE = 131072


def transcribe_file_short(
    file_path: str,
    client: Client,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
) -> Result:
    assert isinstance(file_path, str)

    with open(file_path, "rb") as fh:
        audio = fh.read()

    return transcribe_bytes_short(
        audio,
        client,
        audio_format,
        sample_rate_hertz,
        num_audio_channels,
        speech_context,
    )


def transcribe_bytes_short(
    audio: bytes,
    client: Client,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
) -> Result:
    assert isinstance(audio, bytes)
    assert isinstance(client, Client)
    assert isinstance(sample_rate_hertz, int)
    assert isinstance(num_audio_channels, int)
    assert speech_context is None or isinstance(speech_context, SpeechContext)

    config = TranscribeConfig()
    config.audio_format = audio_format
    config.sample_rate_hertz = sample_rate_hertz
    config.num_audio_channels = num_audio_channels
    if speech_context is not None:
        config.speech_context.CopyFrom(speech_context)

    return client.Transcribe(config, audio)


def transcribe_file_stream(
    file_path: str,
    client: Client,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
) -> Iterable[Result]:
    assert isinstance(file_path, str)

    with open(file_path, "rb") as fh:

        def iter_audio() -> Iterable[bytes]:
            while True:
                audio = fh.read(READ_CHUNK_SIZE)
                if len(audio) == 0:
                    break
                yield audio

        yield from transcribe_iter_bytes_stream(
            iter_audio(),
            client,
            audio_format,
            sample_rate_hertz,
            num_audio_channels,
            speech_context,
        )


def transcribe_bytes_stream(
    audio: bytes,
    client: Client,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
) -> Iterable[Result]:
    assert isinstance(audio, bytes)

    def iter_audio() -> Iterable[bytes]:
        offset = 0
        while offset < len(audio):
            amount = min(READ_CHUNK_SIZE, len(audio) - offset)
            yield audio[offset : offset + amount]
            offset += amount

    yield from transcribe_iter_bytes_stream(
        iter_audio(),
        client,
        audio_format,
        sample_rate_hertz,
        num_audio_channels,
        speech_context,
    )


def transcribe_iter_bytes_stream(
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
    if speech_context is not None:
        config.speech_context.CopyFrom(speech_context)

    yield from client.TranscribeStream(config, iter_audio)

