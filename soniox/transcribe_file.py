from typing import Optional, Iterable, List
from soniox.speech_service import (
    Client,
    Result,
    TranscribeConfig,
    TranscribeStreamConfig,
    SpeechContext,
)

READ_CHUNK_SIZE = 131072


def iter_file_chunks(file_path: str, chunk_size: int = READ_CHUNK_SIZE) -> Iterable[bytes]:
    assert isinstance(file_path, str)
    assert chunk_size > 0

    with open(file_path, "rb") as fh:
        while True:
            data = fh.read(chunk_size)
            if len(data) == 0:
                break
            yield data


def iter_bytes_chunks(data: bytes, chunk_size: int = READ_CHUNK_SIZE) -> Iterable[bytes]:
    assert isinstance(data, bytes)
    assert chunk_size > 0

    offset = 0
    while offset < len(data):
        amount = min(chunk_size, len(data) - offset)
        yield data[offset : offset + amount]
        offset += amount


def transcribe_file_short(
    file_path: str,
    client: Client,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
    enable_profanity_filter: bool = False,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
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
        enable_profanity_filter,
        enable_streaming_speaker_diarization,
        enable_global_speaker_diarization,
        min_num_speakers,
        max_num_speakers,
        enable_speaker_identification,
        cand_speaker_names,
    )


def transcribe_bytes_short(
    audio: bytes,
    client: Client,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
    enable_profanity_filter: bool = False,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
) -> Result:
    assert isinstance(audio, bytes)
    assert isinstance(client, Client)
    assert isinstance(sample_rate_hertz, int)
    assert isinstance(num_audio_channels, int)
    assert speech_context is None or isinstance(speech_context, SpeechContext)
    assert isinstance(enable_profanity_filter, bool)
    assert isinstance(enable_streaming_speaker_diarization, bool)
    assert isinstance(enable_global_speaker_diarization, bool)
    assert isinstance(min_num_speakers, int)
    assert isinstance(max_num_speakers, int)
    assert isinstance(enable_speaker_identification, bool)
    if cand_speaker_names is not None:
        assert isinstance(cand_speaker_names, list)
        assert all(isinstance(name, str) for name in cand_speaker_names)

    config = TranscribeConfig()
    config.audio_format = audio_format
    config.sample_rate_hertz = sample_rate_hertz
    config.num_audio_channels = num_audio_channels
    if speech_context is not None:
        config.speech_context.CopyFrom(speech_context)
    config.enable_profanity_filter = enable_profanity_filter
    config.enable_streaming_speaker_diarization = enable_streaming_speaker_diarization
    config.enable_global_speaker_diarization = enable_global_speaker_diarization
    config.min_num_speakers = min_num_speakers
    config.max_num_speakers = max_num_speakers
    config.enable_speaker_identification = enable_speaker_identification
    if cand_speaker_names is not None:
        config.cand_speaker_names.extend(cand_speaker_names)

    return client.Transcribe(config, audio)


def transcribe_file_stream(
    file_path: str,
    client: Client,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
    enable_profanity_filter: bool = False,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
    chunk_size: int = READ_CHUNK_SIZE,
) -> Iterable[Result]:
    yield from transcribe_iter_bytes_stream(
        iter_file_chunks(file_path, chunk_size),
        client,
        audio_format,
        sample_rate_hertz,
        num_audio_channels,
        speech_context,
        enable_profanity_filter,
        enable_streaming_speaker_diarization,
        enable_global_speaker_diarization,
        min_num_speakers,
        max_num_speakers,
        enable_speaker_identification,
        cand_speaker_names,
    )


def transcribe_bytes_stream(
    audio: bytes,
    client: Client,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
    enable_profanity_filter: bool = False,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
    chunk_size: int = READ_CHUNK_SIZE,
) -> Iterable[Result]:
    yield from transcribe_iter_bytes_stream(
        iter_bytes_chunks(audio, chunk_size),
        client,
        audio_format,
        sample_rate_hertz,
        num_audio_channels,
        speech_context,
        enable_profanity_filter,
        enable_streaming_speaker_diarization,
        enable_global_speaker_diarization,
        min_num_speakers,
        max_num_speakers,
        enable_speaker_identification,
        cand_speaker_names,
    )


def transcribe_iter_bytes_stream(
    iter_audio: Iterable[bytes],
    client: Client,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
    enable_profanity_filter: bool = False,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
) -> Iterable[Result]:
    assert isinstance(client, Client)
    assert isinstance(sample_rate_hertz, int)
    assert isinstance(num_audio_channels, int)
    assert speech_context is None or isinstance(speech_context, SpeechContext)
    assert isinstance(enable_profanity_filter, bool)
    assert isinstance(enable_streaming_speaker_diarization, bool)
    assert isinstance(enable_global_speaker_diarization, bool)
    assert isinstance(min_num_speakers, int)
    assert isinstance(max_num_speakers, int)
    assert isinstance(enable_speaker_identification, bool)
    if cand_speaker_names is not None:
        assert isinstance(cand_speaker_names, list)
        assert all(isinstance(name, str) for name in cand_speaker_names)

    config = TranscribeStreamConfig()
    config.audio_format = audio_format
    config.sample_rate_hertz = sample_rate_hertz
    config.num_audio_channels = num_audio_channels
    if speech_context is not None:
        config.speech_context.CopyFrom(speech_context)
    config.enable_profanity_filter = enable_profanity_filter
    config.enable_streaming_speaker_diarization = enable_streaming_speaker_diarization
    config.enable_global_speaker_diarization = enable_global_speaker_diarization
    config.min_num_speakers = min_num_speakers
    config.max_num_speakers = max_num_speakers
    config.enable_speaker_identification = enable_speaker_identification
    if cand_speaker_names is not None:
        config.cand_speaker_names.extend(cand_speaker_names)

    yield from client.TranscribeStream(config, iter_audio)
