from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddSpeakerAudioRequest(_message.Message):
    __slots__ = ["api_key", "audio", "audio_name", "speaker_name"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_NAME_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_NAME_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    audio: bytes
    audio_name: str
    speaker_name: str
    def __init__(self, api_key: _Optional[str] = ..., speaker_name: _Optional[str] = ..., audio_name: _Optional[str] = ..., audio: _Optional[bytes] = ...) -> None: ...

class AddSpeakerAudioResponse(_message.Message):
    __slots__ = ["audio_name", "created", "duration_ms", "speaker_name"]
    AUDIO_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_NAME_FIELD_NUMBER: _ClassVar[int]
    audio_name: str
    created: _timestamp_pb2.Timestamp
    duration_ms: int
    speaker_name: str
    def __init__(self, speaker_name: _Optional[str] = ..., audio_name: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration_ms: _Optional[int] = ...) -> None: ...

class AddSpeakerRequest(_message.Message):
    __slots__ = ["api_key", "name"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    name: str
    def __init__(self, api_key: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AddSpeakerResponse(_message.Message):
    __slots__ = ["created", "name"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    created: _timestamp_pb2.Timestamp
    name: str
    def __init__(self, name: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateSpeechContextRequest(_message.Message):
    __slots__ = ["api_key", "speech_context"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    SPEECH_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    speech_context: SpeechContext
    def __init__(self, api_key: _Optional[str] = ..., speech_context: _Optional[_Union[SpeechContext, _Mapping]] = ...) -> None: ...

class CreateSpeechContextResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteObjectRequest(_message.Message):
    __slots__ = ["api_key", "object_id"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    object_id: str
    def __init__(self, api_key: _Optional[str] = ..., object_id: _Optional[str] = ...) -> None: ...

class DeleteObjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteSpeechContextRequest(_message.Message):
    __slots__ = ["api_key", "name"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    name: str
    def __init__(self, api_key: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DeleteSpeechContextResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteTranscribeAsyncFileRequest(_message.Message):
    __slots__ = ["api_key", "file_id"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    file_id: str
    def __init__(self, api_key: _Optional[str] = ..., file_id: _Optional[str] = ...) -> None: ...

class DeleteTranscribeAsyncFileResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAudioRequest(_message.Message):
    __slots__ = ["api_key", "audio_bytes_format", "object_id", "time_segment", "token_segment"]
    class TimeSegment(_message.Message):
        __slots__ = ["duration_ms", "start_ms"]
        DURATION_MS_FIELD_NUMBER: _ClassVar[int]
        START_MS_FIELD_NUMBER: _ClassVar[int]
        duration_ms: int
        start_ms: int
        def __init__(self, start_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ...) -> None: ...
    class TokenSegment(_message.Message):
        __slots__ = ["token_end", "token_start"]
        TOKEN_END_FIELD_NUMBER: _ClassVar[int]
        TOKEN_START_FIELD_NUMBER: _ClassVar[int]
        token_end: int
        token_start: int
        def __init__(self, token_start: _Optional[int] = ..., token_end: _Optional[int] = ...) -> None: ...
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    AUDIO_BYTES_FORMAT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    audio_bytes_format: str
    object_id: str
    time_segment: GetAudioRequest.TimeSegment
    token_segment: GetAudioRequest.TokenSegment
    def __init__(self, api_key: _Optional[str] = ..., object_id: _Optional[str] = ..., time_segment: _Optional[_Union[GetAudioRequest.TimeSegment, _Mapping]] = ..., token_segment: _Optional[_Union[GetAudioRequest.TokenSegment, _Mapping]] = ..., audio_bytes_format: _Optional[str] = ...) -> None: ...

class GetAudioResponse(_message.Message):
    __slots__ = ["data", "duration_ms", "num_audio_channels", "object_id", "start_ms", "total_duration_ms"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    NUM_AUDIO_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    START_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    duration_ms: int
    num_audio_channels: int
    object_id: str
    start_ms: int
    total_duration_ms: int
    def __init__(self, object_id: _Optional[str] = ..., start_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ..., total_duration_ms: _Optional[int] = ..., num_audio_channels: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class GetObjectRequest(_message.Message):
    __slots__ = ["api_key", "object_id"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    object_id: str
    def __init__(self, api_key: _Optional[str] = ..., object_id: _Optional[str] = ...) -> None: ...

class GetObjectResponse(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: StoredObject
    def __init__(self, object: _Optional[_Union[StoredObject, _Mapping]] = ...) -> None: ...

class GetSpeakerAudioRequest(_message.Message):
    __slots__ = ["api_key", "audio_name", "speaker_name"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    AUDIO_NAME_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_NAME_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    audio_name: str
    speaker_name: str
    def __init__(self, api_key: _Optional[str] = ..., speaker_name: _Optional[str] = ..., audio_name: _Optional[str] = ...) -> None: ...

class GetSpeakerAudioResponse(_message.Message):
    __slots__ = ["audio", "audio_name", "created", "duration_ms", "speaker_name"]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_NAME_FIELD_NUMBER: _ClassVar[int]
    audio: bytes
    audio_name: str
    created: _timestamp_pb2.Timestamp
    duration_ms: int
    speaker_name: str
    def __init__(self, speaker_name: _Optional[str] = ..., audio_name: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration_ms: _Optional[int] = ..., audio: _Optional[bytes] = ...) -> None: ...

class GetSpeakerRequest(_message.Message):
    __slots__ = ["api_key", "name"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    name: str
    def __init__(self, api_key: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetSpeakerResponse(_message.Message):
    __slots__ = ["audios", "created", "name"]
    AUDIOS_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    audios: _containers.RepeatedCompositeFieldContainer[GetSpeakerResponseAudio]
    created: _timestamp_pb2.Timestamp
    name: str
    def __init__(self, name: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., audios: _Optional[_Iterable[_Union[GetSpeakerResponseAudio, _Mapping]]] = ...) -> None: ...

class GetSpeakerResponseAudio(_message.Message):
    __slots__ = ["audio_name", "created", "duration_ms"]
    AUDIO_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    audio_name: str
    created: _timestamp_pb2.Timestamp
    duration_ms: int
    def __init__(self, audio_name: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration_ms: _Optional[int] = ...) -> None: ...

class GetSpeechContextRequest(_message.Message):
    __slots__ = ["api_key", "name"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    name: str
    def __init__(self, api_key: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetSpeechContextResponse(_message.Message):
    __slots__ = ["speech_context"]
    SPEECH_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    speech_context: SpeechContext
    def __init__(self, speech_context: _Optional[_Union[SpeechContext, _Mapping]] = ...) -> None: ...

class GetTranscribeAsyncResultRequest(_message.Message):
    __slots__ = ["api_key", "file_id"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    file_id: str
    def __init__(self, api_key: _Optional[str] = ..., file_id: _Optional[str] = ...) -> None: ...

class GetTranscribeAsyncResultResponse(_message.Message):
    __slots__ = ["metadata", "result", "separate_recognition_per_channel"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SEPARATE_RECOGNITION_PER_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    metadata: TranscriptionMetadata
    result: Result
    separate_recognition_per_channel: bool
    def __init__(self, separate_recognition_per_channel: bool = ..., result: _Optional[_Union[Result, _Mapping]] = ..., metadata: _Optional[_Union[TranscriptionMetadata, _Mapping]] = ...) -> None: ...

class GetTranscribeAsyncStatusRequest(_message.Message):
    __slots__ = ["api_key", "file_id"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    file_id: str
    def __init__(self, api_key: _Optional[str] = ..., file_id: _Optional[str] = ...) -> None: ...

class GetTranscribeAsyncStatusResponse(_message.Message):
    __slots__ = ["files"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[TranscribeAsyncFileStatus]
    def __init__(self, files: _Optional[_Iterable[_Union[TranscribeAsyncFileStatus, _Mapping]]] = ...) -> None: ...

class Keyterm(_message.Message):
    __slots__ = ["score", "text", "token_start_indexes"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_START_INDEXES_FIELD_NUMBER: _ClassVar[int]
    score: float
    text: str
    token_start_indexes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, text: _Optional[str] = ..., score: _Optional[float] = ..., token_start_indexes: _Optional[_Iterable[int]] = ...) -> None: ...

class ListObjectsRequest(_message.Message):
    __slots__ = ["api_key", "num", "start", "stored_datetime_from", "stored_datetime_to"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STORED_DATETIME_FROM_FIELD_NUMBER: _ClassVar[int]
    STORED_DATETIME_TO_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    num: int
    start: int
    stored_datetime_from: _timestamp_pb2.Timestamp
    stored_datetime_to: _timestamp_pb2.Timestamp
    def __init__(self, api_key: _Optional[str] = ..., stored_datetime_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., stored_datetime_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class ListObjectsResponse(_message.Message):
    __slots__ = ["objects", "start"]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[ListObjectsResponseObject]
    start: int
    def __init__(self, start: _Optional[int] = ..., objects: _Optional[_Iterable[_Union[ListObjectsResponseObject, _Mapping]]] = ...) -> None: ...

class ListObjectsResponseObject(_message.Message):
    __slots__ = ["audio_duration_ms", "audio_stored", "object_id", "stored_audio_ms", "stored_datetime", "transcript_stored"]
    AUDIO_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_STORED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    STORED_AUDIO_MS_FIELD_NUMBER: _ClassVar[int]
    STORED_DATETIME_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_STORED_FIELD_NUMBER: _ClassVar[int]
    audio_duration_ms: int
    audio_stored: bool
    object_id: str
    stored_audio_ms: int
    stored_datetime: _timestamp_pb2.Timestamp
    transcript_stored: bool
    def __init__(self, object_id: _Optional[str] = ..., stored_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., audio_stored: bool = ..., transcript_stored: bool = ..., audio_duration_ms: _Optional[int] = ..., stored_audio_ms: _Optional[int] = ...) -> None: ...

class ListSpeakersRequest(_message.Message):
    __slots__ = ["api_key"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    def __init__(self, api_key: _Optional[str] = ...) -> None: ...

class ListSpeakersResponse(_message.Message):
    __slots__ = ["speakers"]
    SPEAKERS_FIELD_NUMBER: _ClassVar[int]
    speakers: _containers.RepeatedCompositeFieldContainer[ListSpeakersResponseSpeaker]
    def __init__(self, speakers: _Optional[_Iterable[_Union[ListSpeakersResponseSpeaker, _Mapping]]] = ...) -> None: ...

class ListSpeakersResponseSpeaker(_message.Message):
    __slots__ = ["created", "name", "num_audios"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_AUDIOS_FIELD_NUMBER: _ClassVar[int]
    created: _timestamp_pb2.Timestamp
    name: str
    num_audios: int
    def __init__(self, name: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., num_audios: _Optional[int] = ...) -> None: ...

class ListSpeechContextNamesRequest(_message.Message):
    __slots__ = ["api_key"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    def __init__(self, api_key: _Optional[str] = ...) -> None: ...

class ListSpeechContextNamesResponse(_message.Message):
    __slots__ = ["names"]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...

class Paragraph(_message.Message):
    __slots__ = ["sentence_end", "sentence_start"]
    SENTENCE_END_FIELD_NUMBER: _ClassVar[int]
    SENTENCE_START_FIELD_NUMBER: _ClassVar[int]
    sentence_end: int
    sentence_start: int
    def __init__(self, sentence_start: _Optional[int] = ..., sentence_end: _Optional[int] = ...) -> None: ...

class RemoveSpeakerAudioRequest(_message.Message):
    __slots__ = ["api_key", "audio_name", "speaker_name"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    AUDIO_NAME_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_NAME_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    audio_name: str
    speaker_name: str
    def __init__(self, api_key: _Optional[str] = ..., speaker_name: _Optional[str] = ..., audio_name: _Optional[str] = ...) -> None: ...

class RemoveSpeakerAudioResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemoveSpeakerRequest(_message.Message):
    __slots__ = ["api_key", "name"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    name: str
    def __init__(self, api_key: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class RemoveSpeakerResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Result(_message.Message):
    __slots__ = ["channel", "final_proc_time_ms", "speakers", "total_proc_time_ms", "words"]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    FINAL_PROC_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    SPEAKERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PROC_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    WORDS_FIELD_NUMBER: _ClassVar[int]
    channel: int
    final_proc_time_ms: int
    speakers: _containers.RepeatedCompositeFieldContainer[ResultSpeaker]
    total_proc_time_ms: int
    words: _containers.RepeatedCompositeFieldContainer[Word]
    def __init__(self, words: _Optional[_Iterable[_Union[Word, _Mapping]]] = ..., final_proc_time_ms: _Optional[int] = ..., total_proc_time_ms: _Optional[int] = ..., speakers: _Optional[_Iterable[_Union[ResultSpeaker, _Mapping]]] = ..., channel: _Optional[int] = ...) -> None: ...

class ResultSpeaker(_message.Message):
    __slots__ = ["name", "speaker"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    name: str
    speaker: int
    def __init__(self, speaker: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ["api_key", "datetime_from", "datetime_to", "metadata_query", "num", "object_id", "start", "text_query"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FROM_FIELD_NUMBER: _ClassVar[int]
    DATETIME_TO_FIELD_NUMBER: _ClassVar[int]
    METADATA_QUERY_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    TEXT_QUERY_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    datetime_from: _timestamp_pb2.Timestamp
    datetime_to: _timestamp_pb2.Timestamp
    metadata_query: str
    num: int
    object_id: str
    start: int
    text_query: str
    def __init__(self, api_key: _Optional[str] = ..., object_id: _Optional[str] = ..., metadata_query: _Optional[str] = ..., datetime_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., datetime_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., text_query: _Optional[str] = ..., start: _Optional[int] = ..., num: _Optional[int] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ["num_found", "results", "start"]
    NUM_FOUND_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    num_found: int
    results: _containers.RepeatedCompositeFieldContainer[SearchResult]
    start: int
    def __init__(self, num_found: _Optional[int] = ..., start: _Optional[int] = ..., results: _Optional[_Iterable[_Union[SearchResult, _Mapping]]] = ...) -> None: ...

class SearchResult(_message.Message):
    __slots__ = ["datetime", "duration_ms", "metadata", "object_id", "preview", "title"]
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    datetime: _timestamp_pb2.Timestamp
    duration_ms: int
    metadata: _containers.ScalarMap[str, str]
    object_id: str
    preview: str
    title: str
    def __init__(self, object_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., title: _Optional[str] = ..., datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration_ms: _Optional[int] = ..., preview: _Optional[str] = ...) -> None: ...

class Sentence(_message.Message):
    __slots__ = ["token_end", "token_start"]
    TOKEN_END_FIELD_NUMBER: _ClassVar[int]
    TOKEN_START_FIELD_NUMBER: _ClassVar[int]
    token_end: int
    token_start: int
    def __init__(self, token_start: _Optional[int] = ..., token_end: _Optional[int] = ...) -> None: ...

class SpeechContext(_message.Message):
    __slots__ = ["entries", "name"]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[SpeechContextEntry]
    name: str
    def __init__(self, entries: _Optional[_Iterable[_Union[SpeechContextEntry, _Mapping]]] = ..., name: _Optional[str] = ...) -> None: ...

class SpeechContextEntry(_message.Message):
    __slots__ = ["boost", "phrases"]
    BOOST_FIELD_NUMBER: _ClassVar[int]
    PHRASES_FIELD_NUMBER: _ClassVar[int]
    boost: float
    phrases: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, phrases: _Optional[_Iterable[str]] = ..., boost: _Optional[float] = ...) -> None: ...

class StorageConfig(_message.Message):
    __slots__ = ["datetime", "disable_store_audio", "disable_store_transcript", "metadata", "object_id", "title"]
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    DISABLE_STORE_AUDIO_FIELD_NUMBER: _ClassVar[int]
    DISABLE_STORE_TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    datetime: _timestamp_pb2.Timestamp
    disable_store_audio: bool
    disable_store_transcript: bool
    metadata: _containers.ScalarMap[str, str]
    object_id: str
    title: str
    def __init__(self, object_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., title: _Optional[str] = ..., datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., disable_store_audio: bool = ..., disable_store_transcript: bool = ...) -> None: ...

class StoredObject(_message.Message):
    __slots__ = ["audio_stored", "datetime", "duration_ms", "metadata", "num_audio_channels", "object_id", "stored_datetime", "title", "transcript"]
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AUDIO_STORED_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NUM_AUDIO_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    STORED_DATETIME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    audio_stored: bool
    datetime: _timestamp_pb2.Timestamp
    duration_ms: int
    metadata: _containers.ScalarMap[str, str]
    num_audio_channels: int
    object_id: str
    stored_datetime: _timestamp_pb2.Timestamp
    title: str
    transcript: Transcript
    def __init__(self, object_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., title: _Optional[str] = ..., datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., stored_datetime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration_ms: _Optional[int] = ..., num_audio_channels: _Optional[int] = ..., audio_stored: bool = ..., transcript: _Optional[_Union[Transcript, _Mapping]] = ...) -> None: ...

class Token(_message.Message):
    __slots__ = ["confidence", "duration_ms", "idx", "profane", "speaker_id", "start_ms", "text", "text_end", "text_start"]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    IDX_FIELD_NUMBER: _ClassVar[int]
    PROFANE_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_ID_FIELD_NUMBER: _ClassVar[int]
    START_MS_FIELD_NUMBER: _ClassVar[int]
    TEXT_END_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TEXT_START_FIELD_NUMBER: _ClassVar[int]
    confidence: float
    duration_ms: int
    idx: int
    profane: bool
    speaker_id: int
    start_ms: int
    text: str
    text_end: int
    text_start: int
    def __init__(self, idx: _Optional[int] = ..., text_start: _Optional[int] = ..., text_end: _Optional[int] = ..., text: _Optional[str] = ..., start_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ..., confidence: _Optional[float] = ..., speaker_id: _Optional[int] = ..., profane: bool = ...) -> None: ...

class TranscribeAsyncFileStatus(_message.Message):
    __slots__ = ["created_time", "error_message", "file_id", "reference_name", "status"]
    CREATED_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    created_time: _timestamp_pb2.Timestamp
    error_message: str
    file_id: str
    reference_name: str
    status: str
    def __init__(self, file_id: _Optional[str] = ..., reference_name: _Optional[str] = ..., status: _Optional[str] = ..., created_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error_message: _Optional[str] = ...) -> None: ...

class TranscribeAsyncRequest(_message.Message):
    __slots__ = ["api_key", "audio", "config", "enable_eof", "eof", "reference_name"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_EOF_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    audio: bytes
    config: TranscriptionConfig
    enable_eof: bool
    eof: bool
    reference_name: str
    def __init__(self, api_key: _Optional[str] = ..., reference_name: _Optional[str] = ..., config: _Optional[_Union[TranscriptionConfig, _Mapping]] = ..., enable_eof: bool = ..., eof: bool = ..., audio: _Optional[bytes] = ...) -> None: ...

class TranscribeAsyncResponse(_message.Message):
    __slots__ = ["file_id"]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    def __init__(self, file_id: _Optional[str] = ...) -> None: ...

class TranscribeMeetingRequest(_message.Message):
    __slots__ = ["api_key", "audio", "config", "end_of_segment", "seq_num", "start_of_segment", "stream_id"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    END_OF_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    START_OF_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    audio: bytes
    config: TranscriptionConfig
    end_of_segment: bool
    seq_num: int
    start_of_segment: bool
    stream_id: int
    def __init__(self, api_key: _Optional[str] = ..., config: _Optional[_Union[TranscriptionConfig, _Mapping]] = ..., seq_num: _Optional[int] = ..., stream_id: _Optional[int] = ..., start_of_segment: bool = ..., audio: _Optional[bytes] = ..., end_of_segment: bool = ...) -> None: ...

class TranscribeMeetingResponse(_message.Message):
    __slots__ = ["end_of_segment", "error", "metadata", "result", "seq_num", "start_of_segment", "stream_id"]
    END_OF_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    START_OF_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    end_of_segment: bool
    error: str
    metadata: TranscriptionMetadata
    result: Result
    seq_num: int
    start_of_segment: bool
    stream_id: int
    def __init__(self, seq_num: _Optional[int] = ..., stream_id: _Optional[int] = ..., start_of_segment: bool = ..., end_of_segment: bool = ..., result: _Optional[_Union[Result, _Mapping]] = ..., error: _Optional[str] = ..., metadata: _Optional[_Union[TranscriptionMetadata, _Mapping]] = ...) -> None: ...

class TranscribeRequest(_message.Message):
    __slots__ = ["api_key", "audio", "config"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    audio: bytes
    config: TranscriptionConfig
    def __init__(self, api_key: _Optional[str] = ..., config: _Optional[_Union[TranscriptionConfig, _Mapping]] = ..., audio: _Optional[bytes] = ...) -> None: ...

class TranscribeResponse(_message.Message):
    __slots__ = ["channel_results", "metadata", "result"]
    CHANNEL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    channel_results: _containers.RepeatedCompositeFieldContainer[Result]
    metadata: TranscriptionMetadata
    result: Result
    def __init__(self, result: _Optional[_Union[Result, _Mapping]] = ..., channel_results: _Optional[_Iterable[_Union[Result, _Mapping]]] = ..., metadata: _Optional[_Union[TranscriptionMetadata, _Mapping]] = ...) -> None: ...

class TranscribeStreamRequest(_message.Message):
    __slots__ = ["api_key", "audio", "config"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    audio: bytes
    config: TranscriptionConfig
    def __init__(self, api_key: _Optional[str] = ..., config: _Optional[_Union[TranscriptionConfig, _Mapping]] = ..., audio: _Optional[bytes] = ...) -> None: ...

class TranscribeStreamResponse(_message.Message):
    __slots__ = ["metadata", "result"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    metadata: TranscriptionMetadata
    result: Result
    def __init__(self, result: _Optional[_Union[Result, _Mapping]] = ..., metadata: _Optional[_Union[TranscriptionMetadata, _Mapping]] = ...) -> None: ...

class Transcript(_message.Message):
    __slots__ = ["keyterms", "paragraphs", "sentences", "speaker_names", "text", "tokens"]
    class SpeakerNamesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    KEYTERMS_FIELD_NUMBER: _ClassVar[int]
    PARAGRAPHS_FIELD_NUMBER: _ClassVar[int]
    SENTENCES_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_NAMES_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    keyterms: _containers.RepeatedCompositeFieldContainer[Keyterm]
    paragraphs: _containers.RepeatedCompositeFieldContainer[Paragraph]
    sentences: _containers.RepeatedCompositeFieldContainer[Sentence]
    speaker_names: _containers.ScalarMap[int, str]
    text: str
    tokens: _containers.RepeatedCompositeFieldContainer[Token]
    def __init__(self, text: _Optional[str] = ..., tokens: _Optional[_Iterable[_Union[Token, _Mapping]]] = ..., sentences: _Optional[_Iterable[_Union[Sentence, _Mapping]]] = ..., paragraphs: _Optional[_Iterable[_Union[Paragraph, _Mapping]]] = ..., keyterms: _Optional[_Iterable[_Union[Keyterm, _Mapping]]] = ..., speaker_names: _Optional[_Mapping[int, str]] = ...) -> None: ...

class TranscriptionConfig(_message.Message):
    __slots__ = ["audio_format", "cand_speaker_names", "client_request_reference", "content_moderation_phrases", "enable_dictation", "enable_endpoint_detection", "enable_global_speaker_diarization", "enable_profanity_filter", "enable_separate_recognition_per_channel", "enable_speaker_identification", "enable_streaming_speaker_diarization", "include_nonfinal", "max_num_speakers", "min_num_speakers", "model", "num_audio_channels", "sample_rate_hertz", "speech_context", "storage_config"]
    AUDIO_FORMAT_FIELD_NUMBER: _ClassVar[int]
    CAND_SPEAKER_NAMES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_REQUEST_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MODERATION_PHRASES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DICTATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ENDPOINT_DETECTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_GLOBAL_SPEAKER_DIARIZATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PROFANITY_FILTER_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SEPARATE_RECOGNITION_PER_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SPEAKER_IDENTIFICATION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STREAMING_SPEAKER_DIARIZATION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_NONFINAL_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_SPEAKERS_FIELD_NUMBER: _ClassVar[int]
    MIN_NUM_SPEAKERS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NUM_AUDIO_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_HERTZ_FIELD_NUMBER: _ClassVar[int]
    SPEECH_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    audio_format: str
    cand_speaker_names: _containers.RepeatedScalarFieldContainer[str]
    client_request_reference: str
    content_moderation_phrases: _containers.RepeatedScalarFieldContainer[str]
    enable_dictation: bool
    enable_endpoint_detection: bool
    enable_global_speaker_diarization: bool
    enable_profanity_filter: bool
    enable_separate_recognition_per_channel: bool
    enable_speaker_identification: bool
    enable_streaming_speaker_diarization: bool
    include_nonfinal: bool
    max_num_speakers: int
    min_num_speakers: int
    model: str
    num_audio_channels: int
    sample_rate_hertz: int
    speech_context: SpeechContext
    storage_config: StorageConfig
    def __init__(self, client_request_reference: _Optional[str] = ..., audio_format: _Optional[str] = ..., sample_rate_hertz: _Optional[int] = ..., num_audio_channels: _Optional[int] = ..., include_nonfinal: bool = ..., enable_separate_recognition_per_channel: bool = ..., enable_endpoint_detection: bool = ..., speech_context: _Optional[_Union[SpeechContext, _Mapping]] = ..., enable_profanity_filter: bool = ..., content_moderation_phrases: _Optional[_Iterable[str]] = ..., enable_streaming_speaker_diarization: bool = ..., enable_global_speaker_diarization: bool = ..., min_num_speakers: _Optional[int] = ..., max_num_speakers: _Optional[int] = ..., enable_speaker_identification: bool = ..., cand_speaker_names: _Optional[_Iterable[str]] = ..., model: _Optional[str] = ..., enable_dictation: bool = ..., storage_config: _Optional[_Union[StorageConfig, _Mapping]] = ...) -> None: ...

class TranscriptionMetadata(_message.Message):
    __slots__ = ["package_version"]
    PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    package_version: str
    def __init__(self, package_version: _Optional[str] = ...) -> None: ...

class UpdateSpeechContextRequest(_message.Message):
    __slots__ = ["api_key", "speech_context"]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    SPEECH_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    speech_context: SpeechContext
    def __init__(self, api_key: _Optional[str] = ..., speech_context: _Optional[_Union[SpeechContext, _Mapping]] = ...) -> None: ...

class UpdateSpeechContextResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Word(_message.Message):
    __slots__ = ["confidence", "duration_ms", "is_final", "orig_text", "speaker", "start_ms", "text"]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_FIELD_NUMBER: _ClassVar[int]
    ORIG_TEXT_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    START_MS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    confidence: float
    duration_ms: int
    is_final: bool
    orig_text: str
    speaker: int
    start_ms: int
    text: str
    def __init__(self, text: _Optional[str] = ..., start_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ..., is_final: bool = ..., speaker: _Optional[int] = ..., orig_text: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...
