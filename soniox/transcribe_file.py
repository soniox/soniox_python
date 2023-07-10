from typing import Optional, Iterable, List, Union
from soniox.speech_service import (
    SpeechClient,
    Result,
    TranscriptionConfig,
    SpeechContext,
    StorageConfig,
    DocumentFormattingConfig,
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
    client: SpeechClient,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
    enable_profanity_filter: bool = False,
    content_moderation_phrases: Optional[List[str]] = None,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
    enable_separate_recognition_per_channel: bool = False,
    model: str = "",
    enable_dictation: bool = False,
    enable_endpoint_detection: bool = False,
    storage_config: Optional[StorageConfig] = None,
    client_request_reference: str = "",
) -> Union[Result, List[Result]]:
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
        content_moderation_phrases,
        enable_streaming_speaker_diarization,
        enable_global_speaker_diarization,
        min_num_speakers,
        max_num_speakers,
        enable_speaker_identification,
        cand_speaker_names,
        enable_separate_recognition_per_channel,
        model,
        enable_dictation,
        enable_endpoint_detection,
        storage_config,
        client_request_reference,
    )


def transcribe_bytes_short(
    audio: bytes,
    client: SpeechClient,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
    enable_profanity_filter: bool = False,
    content_moderation_phrases: Optional[List[str]] = None,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
    enable_separate_recognition_per_channel: bool = False,
    model: str = "",
    enable_dictation: bool = False,
    enable_endpoint_detection: bool = False,
    storage_config: Optional[StorageConfig] = None,
    client_request_reference: str = "",
) -> Union[Result, List[Result]]:
    assert isinstance(audio, bytes)
    assert isinstance(client, SpeechClient)
    assert isinstance(sample_rate_hertz, int)
    assert isinstance(num_audio_channels, int)
    assert speech_context is None or isinstance(speech_context, SpeechContext)
    assert isinstance(enable_profanity_filter, bool)
    if content_moderation_phrases is not None:
        assert isinstance(content_moderation_phrases, list)
        assert all(isinstance(phrase, str) for phrase in content_moderation_phrases)
    assert isinstance(enable_streaming_speaker_diarization, bool)
    assert isinstance(enable_global_speaker_diarization, bool)
    assert isinstance(min_num_speakers, int)
    assert isinstance(max_num_speakers, int)
    assert isinstance(enable_speaker_identification, bool)
    if cand_speaker_names is not None:
        assert isinstance(cand_speaker_names, list)
        assert all(isinstance(name, str) for name in cand_speaker_names)
    assert isinstance(enable_separate_recognition_per_channel, bool)
    assert isinstance(model, str)
    assert isinstance(enable_dictation, bool)
    assert isinstance(enable_endpoint_detection, bool)
    assert storage_config is None or isinstance(storage_config, StorageConfig)
    assert isinstance(client_request_reference, str)

    config = TranscriptionConfig()
    config.audio_format = audio_format
    config.sample_rate_hertz = sample_rate_hertz
    config.num_audio_channels = num_audio_channels
    if speech_context is not None:
        config.speech_context.CopyFrom(speech_context)
    config.enable_profanity_filter = enable_profanity_filter
    if content_moderation_phrases is not None:
        config.content_moderation_phrases.extend(content_moderation_phrases)
    config.enable_streaming_speaker_diarization = enable_streaming_speaker_diarization
    config.enable_global_speaker_diarization = enable_global_speaker_diarization
    config.min_num_speakers = min_num_speakers
    config.max_num_speakers = max_num_speakers
    config.enable_speaker_identification = enable_speaker_identification
    if cand_speaker_names is not None:
        config.cand_speaker_names.extend(cand_speaker_names)
    config.enable_separate_recognition_per_channel = enable_separate_recognition_per_channel
    config.model = model
    config.enable_dictation = enable_dictation
    config.enable_endpoint_detection = enable_endpoint_detection
    if storage_config is not None:
        config.storage_config.CopyFrom(storage_config)
    config.client_request_reference = client_request_reference

    return client.Transcribe(config, audio)


def transcribe_file_stream(
    file_path: str,
    client: SpeechClient,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
    enable_profanity_filter: bool = False,
    content_moderation_phrases: Optional[List[str]] = None,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
    enable_separate_recognition_per_channel: bool = False,
    model: str = "",
    enable_dictation: bool = False,
    enable_endpoint_detection: bool = False,
    storage_config: Optional[StorageConfig] = None,
    client_request_reference: str = "",
    chunk_size: int = READ_CHUNK_SIZE,
) -> Union[Result, List[Result]]:
    return transcribe_iter_bytes_stream(
        iter_file_chunks(file_path, chunk_size),
        client,
        audio_format,
        sample_rate_hertz,
        num_audio_channels,
        speech_context,
        enable_profanity_filter,
        content_moderation_phrases,
        enable_streaming_speaker_diarization,
        enable_global_speaker_diarization,
        min_num_speakers,
        max_num_speakers,
        enable_speaker_identification,
        cand_speaker_names,
        enable_separate_recognition_per_channel,
        model,
        enable_dictation,
        enable_endpoint_detection,
        storage_config,
        client_request_reference,
    )


def transcribe_bytes_stream(
    audio: bytes,
    client: SpeechClient,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
    enable_profanity_filter: bool = False,
    content_moderation_phrases: Optional[List[str]] = None,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
    enable_separate_recognition_per_channel: bool = False,
    model: str = "",
    enable_dictation: bool = False,
    enable_endpoint_detection: bool = False,
    storage_config: Optional[StorageConfig] = None,
    client_request_reference: str = "",
    chunk_size: int = READ_CHUNK_SIZE,
) -> Union[Result, List[Result]]:
    return transcribe_iter_bytes_stream(
        iter_bytes_chunks(audio, chunk_size),
        client,
        audio_format,
        sample_rate_hertz,
        num_audio_channels,
        speech_context,
        enable_profanity_filter,
        content_moderation_phrases,
        enable_streaming_speaker_diarization,
        enable_global_speaker_diarization,
        min_num_speakers,
        max_num_speakers,
        enable_speaker_identification,
        cand_speaker_names,
        enable_separate_recognition_per_channel,
        model,
        enable_dictation,
        enable_endpoint_detection,
        storage_config,
        client_request_reference,
    )


def transcribe_iter_bytes_stream(
    iter_audio: Iterable[bytes],
    client: SpeechClient,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
    enable_profanity_filter: bool = False,
    content_moderation_phrases: Optional[List[str]] = None,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
    enable_separate_recognition_per_channel: bool = False,
    model: str = "",
    enable_dictation: bool = False,
    enable_endpoint_detection: bool = False,
    storage_config: Optional[StorageConfig] = None,
    client_request_reference: str = "",
) -> Union[Result, List[Result]]:
    assert isinstance(client, SpeechClient)
    assert isinstance(sample_rate_hertz, int)
    assert isinstance(num_audio_channels, int)
    assert speech_context is None or isinstance(speech_context, SpeechContext)
    assert isinstance(enable_profanity_filter, bool)
    if content_moderation_phrases is not None:
        assert isinstance(content_moderation_phrases, list)
        assert all(isinstance(phrase, str) for phrase in content_moderation_phrases)
    assert isinstance(enable_streaming_speaker_diarization, bool)
    assert isinstance(enable_global_speaker_diarization, bool)
    assert isinstance(min_num_speakers, int)
    assert isinstance(max_num_speakers, int)
    assert isinstance(enable_speaker_identification, bool)
    if cand_speaker_names is not None:
        assert isinstance(cand_speaker_names, list)
        assert all(isinstance(name, str) for name in cand_speaker_names)
    assert isinstance(enable_separate_recognition_per_channel, bool)
    assert isinstance(model, str)
    assert isinstance(enable_dictation, bool)
    assert isinstance(enable_endpoint_detection, bool)
    assert storage_config is None or isinstance(storage_config, StorageConfig)
    assert isinstance(client_request_reference, str)

    config = TranscriptionConfig()
    config.audio_format = audio_format
    config.sample_rate_hertz = sample_rate_hertz
    config.num_audio_channels = num_audio_channels
    if speech_context is not None:
        config.speech_context.CopyFrom(speech_context)
    config.enable_profanity_filter = enable_profanity_filter
    if content_moderation_phrases is not None:
        config.content_moderation_phrases.extend(content_moderation_phrases)
    config.enable_streaming_speaker_diarization = enable_streaming_speaker_diarization
    config.enable_global_speaker_diarization = enable_global_speaker_diarization
    config.min_num_speakers = min_num_speakers
    config.max_num_speakers = max_num_speakers
    config.enable_speaker_identification = enable_speaker_identification
    if cand_speaker_names is not None:
        config.cand_speaker_names.extend(cand_speaker_names)
    config.enable_separate_recognition_per_channel = enable_separate_recognition_per_channel
    config.model = model
    config.enable_dictation = enable_dictation
    config.enable_endpoint_detection = enable_endpoint_detection
    if storage_config is not None:
        config.storage_config.CopyFrom(storage_config)
    config.client_request_reference = client_request_reference

    return client.TranscribeCompleteStream(config, iter_audio)


def transcribe_file_async(
    file_path: str,
    client: SpeechClient,
    audio_format: str = "",
    sample_rate_hertz: int = 0,
    num_audio_channels: int = 0,
    speech_context: Optional[SpeechContext] = None,
    enable_profanity_filter: bool = False,
    content_moderation_phrases: Optional[List[str]] = None,
    enable_streaming_speaker_diarization: bool = False,
    enable_global_speaker_diarization: bool = False,
    min_num_speakers: int = 0,
    max_num_speakers: int = 0,
    enable_speaker_identification: bool = False,
    cand_speaker_names: Optional[List[str]] = None,
    enable_separate_recognition_per_channel: bool = False,
    model: str = "",
    enable_dictation: bool = False,
    enable_endpoint_detection: bool = False,
    reference_name: str = "",
    storage_config: Optional[StorageConfig] = None,
    document_formatting_config: Optional[DocumentFormattingConfig] = None,
    client_request_reference: str = "",
    chunk_size: int = READ_CHUNK_SIZE,
) -> str:
    assert isinstance(client, SpeechClient)
    assert isinstance(sample_rate_hertz, int)
    assert isinstance(num_audio_channels, int)
    assert speech_context is None or isinstance(speech_context, SpeechContext)
    assert isinstance(enable_profanity_filter, bool)
    if content_moderation_phrases is not None:
        assert isinstance(content_moderation_phrases, list)
        assert all(isinstance(phrase, str) for phrase in content_moderation_phrases)
    assert isinstance(enable_streaming_speaker_diarization, bool)
    assert isinstance(enable_global_speaker_diarization, bool)
    assert isinstance(min_num_speakers, int)
    assert isinstance(max_num_speakers, int)
    assert isinstance(enable_speaker_identification, bool)
    if cand_speaker_names is not None:
        assert isinstance(cand_speaker_names, list)
        assert all(isinstance(name, str) for name in cand_speaker_names)
    assert isinstance(enable_separate_recognition_per_channel, bool)
    assert isinstance(model, str)
    assert isinstance(enable_dictation, bool)
    assert isinstance(enable_endpoint_detection, bool)
    assert storage_config is None or isinstance(storage_config, StorageConfig)
    assert document_formatting_config is None or isinstance(
        document_formatting_config, DocumentFormattingConfig
    )
    assert isinstance(reference_name, str)
    assert isinstance(client_request_reference, str)

    config = TranscriptionConfig()
    config.audio_format = audio_format
    config.sample_rate_hertz = sample_rate_hertz
    config.num_audio_channels = num_audio_channels
    if speech_context is not None:
        config.speech_context.CopyFrom(speech_context)
    config.enable_profanity_filter = enable_profanity_filter
    if content_moderation_phrases is not None:
        config.content_moderation_phrases.extend(content_moderation_phrases)
    config.enable_streaming_speaker_diarization = enable_streaming_speaker_diarization
    config.enable_global_speaker_diarization = enable_global_speaker_diarization
    config.min_num_speakers = min_num_speakers
    config.max_num_speakers = max_num_speakers
    config.enable_speaker_identification = enable_speaker_identification
    if cand_speaker_names is not None:
        config.cand_speaker_names.extend(cand_speaker_names)
    config.enable_separate_recognition_per_channel = enable_separate_recognition_per_channel
    config.model = model
    config.enable_dictation = enable_dictation
    config.enable_endpoint_detection = enable_endpoint_detection
    if storage_config is not None:
        config.storage_config.CopyFrom(storage_config)
    if document_formatting_config is not None:
        config.document_formatting_config.CopyFrom(document_formatting_config)
    config.client_request_reference = client_request_reference

    return client.TranscribeAsync(reference_name, iter_file_chunks(file_path, chunk_size), config)
