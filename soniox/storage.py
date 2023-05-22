from typing import Iterable, Optional
from datetime import datetime

from google.protobuf.timestamp_pb2 import Timestamp as ProtoTimestamp

from soniox.speech_service import SpeechClient
from soniox.speech_service_pb2 import (
    StoredObject,
    GetObjectRequest,
    ListObjectsRequest,
    ListObjectsResponse,
    DeleteObjectRequest,
    GetAudioRequest,
    GetAudioResponse,
    SearchRequest,
    SearchResponse,
)


def get_object(object_id: str, client: SpeechClient) -> StoredObject:
    assert isinstance(object_id, str) and len(object_id) > 0
    assert isinstance(client, SpeechClient)

    response = client.service_stub.GetObject(
        GetObjectRequest(api_key=client.api_key, object_id=object_id)
    )
    stored_object = response.object

    return stored_object


def delete_object(object_id: str, client: SpeechClient) -> None:
    assert isinstance(object_id, str) and len(object_id) > 0
    assert isinstance(client, SpeechClient)

    client.service_stub.DeleteObject(
        DeleteObjectRequest(api_key=client.api_key, object_id=object_id)
    )


def list_objects(
    client: SpeechClient,
    stored_datetime_from: Optional[datetime] = None,
    stored_datetime_to: Optional[datetime] = None,
    start: int = 0,
    num: int = 0,
) -> ListObjectsResponse:
    assert isinstance(client, SpeechClient)
    assert stored_datetime_from is None or isinstance(stored_datetime_from, datetime)
    assert stored_datetime_to is None or isinstance(stored_datetime_to, datetime)
    assert isinstance(start, int) and start >= 0
    assert isinstance(num, int) and num >= 0

    proto_stored_datetime_from = None
    proto_stored_datetime_to = None
    if stored_datetime_from is not None:
        proto_stored_datetime_from = ProtoTimestamp()
        proto_stored_datetime_from.FromDatetime(stored_datetime_from)
    if stored_datetime_to is not None:
        proto_stored_datetime_to = ProtoTimestamp()
        proto_stored_datetime_to.FromDatetime(stored_datetime_to)

    response = client.service_stub.ListObjects(
        ListObjectsRequest(
            api_key=client.api_key,
            stored_datetime_from=proto_stored_datetime_from,
            stored_datetime_to=proto_stored_datetime_to,
            start=start,
            num=num,
        )
    )

    return response


def search_objects(
    client: SpeechClient,
    object_id: Optional[str] = None,
    metadata_query: Optional[str] = None,
    datetime_from: Optional[datetime] = None,
    datetime_to: Optional[datetime] = None,
    text_query: Optional[str] = None,
    start: int = 0,
    num: int = 0,
) -> SearchResponse:
    assert isinstance(client, SpeechClient)
    assert object_id is None or isinstance(object_id, str)
    assert metadata_query is None or isinstance(metadata_query, str)
    assert datetime_from is None or isinstance(datetime_from, datetime)
    assert datetime_to is None or isinstance(datetime_to, datetime)
    assert text_query is None or isinstance(text_query, str)
    assert isinstance(start, int) and start >= 0
    assert isinstance(num, int) and num >= 0

    proto_datetime_from = None
    proto_datetime_to = None

    if object_id is None:
        object_id = ""
    if metadata_query is None:
        metadata_query = ""
    if datetime_from is not None:
        proto_datetime_from = ProtoTimestamp()
        proto_datetime_from.FromDatetime(datetime_from)
    if datetime_to is not None:
        proto_datetime_to = ProtoTimestamp()
        proto_datetime_to.FromDatetime(datetime_to)
    if text_query is None:
        text_query = ""

    response = client.service_stub.Search(
        SearchRequest(
            api_key=client.api_key,
            object_id=object_id,
            metadata_query=metadata_query,
            datetime_from=proto_datetime_from,
            datetime_to=proto_datetime_to,
            text_query=text_query,
            start=start,
            num=num,
        )
    )

    return response


def get_audio(
    object_id: str,
    client: SpeechClient,
    start_ms: Optional[int] = None,
    duration_ms: Optional[int] = None,
    token_start: Optional[int] = None,
    token_end: Optional[int] = None,
    audio_bytes_format: Optional[str] = None,
) -> Iterable[GetAudioResponse]:
    assert isinstance(object_id, str) and len(object_id) > 0
    assert isinstance(client, SpeechClient)
    assert audio_bytes_format is None or isinstance(audio_bytes_format, str)

    time_segment = None
    token_segment = None
    cannot_both_err = "cannot specify time and token range at the same time"
    if start_ms is not None:
        assert duration_ms is not None, "duration_ms is required if start_ms is specified"
        assert isinstance(start_ms, int)
        assert isinstance(duration_ms, int)
        assert start_ms >= 0
        assert duration_ms >= 0
        assert token_start is None, cannot_both_err
        assert token_end is None, cannot_both_err
        time_segment = GetAudioRequest.TimeSegment(
            start_ms=start_ms,
            duration_ms=duration_ms,
        )
    elif token_start is not None:
        assert token_end is not None
        assert isinstance(token_start, int)
        assert isinstance(token_end, int)
        assert token_start >= 0
        assert token_end > token_start
        assert start_ms is None, cannot_both_err
        assert duration_ms is None, cannot_both_err
        token_segment = GetAudioRequest.TokenSegment(
            token_start=token_start,
            token_end=token_end,
        )
    else:
        raise Exception("neither time nor token range specified")

    return client.service_stub.GetAudio(
        GetAudioRequest(
            api_key=client.api_key,
            object_id=object_id,
            time_segment=time_segment,
            token_segment=token_segment,
            audio_bytes_format=audio_bytes_format,
        )
    )
