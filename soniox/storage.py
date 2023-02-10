from datetime import datetime
from typing import Iterable, Optional
from soniox.speech_service import (
    SpeechClient,
)
from soniox.speech_service_pb2 import (
    GetAudioRequest,
    GetAudioResponse,
    SearchRequest,
    SearchResponse,
    StoredObject,
    GetObjectRequest,
)
from google.protobuf.timestamp_pb2 import Timestamp as ProtoTimestamp


def get_object(object_id: str, client: SpeechClient) -> StoredObject:
    assert isinstance(object_id, str) and len(object_id) > 0
    assert isinstance(client, SpeechClient)

    response = client.service_stub.GetObject(GetObjectRequest(
        api_key=client.api_key,
        object_id=object_id
    ))
    stored_object = response.object

    return stored_object

def search_objects(
    client: SpeechClient,
    object_id: Optional[str] = None,
    metadata_query: Optional[str] = None,
    datetime_from: Optional[datetime] = None,
    datetime_to: Optional[datetime] = None,
    text_query: Optional[str] = None,
    start: int = 0,
    num: int = -1,
) -> SearchResponse:
    '''
        Searches and retrieves objects from Soniox Storage. It allows search by the client
        assigned `object_id`, the object metadata, date and text query. Parameters `start`
        and `num` define the index of the first returned result (offset) and number of returned
        results (limit) respectively.

        Search over metadata is supported by a simple boolean grammar that supports conjuntion,
        disjunction and nesting. An example metadata query is presented below.

        Let the stored metadata dictionary be:
        {
            "key1": "val1",
            "key2": "val2",
            "key3": "val3
        }

        The metadata query language supports expressions of the form:
        (key1 = val1 OR key2 = someval) AND key3 = val3

        AND / OR can be used interchangeably with && / ||
    
    '''
    assert isinstance(client, SpeechClient)
    assert object_id is None or isinstance(object_id, str)
    assert metadata_query is None or isinstance(metadata_query, str)
    assert datetime_from is None or isinstance(datetime_from, datetime)
    assert datetime_to is None or isinstance(datetime_to, datetime)
    assert text_query is None or isinstance(text_query, str)
    assert isinstance(start, int) and start >= 0
    assert isinstance(num, int) and num >= -1

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
            start=start,
            num=num
        )
    )

    return response
    

def get_audio_time_segment(
    object_id: str,
    client: SpeechClient,
    start_ms: int,
    duration_ms: int,
    audio_bytes_format: Optional[str] = None
) -> Iterable[GetAudioResponse]:
    assert isinstance(object_id, str) and len(object_id) > 0
    assert isinstance(client, SpeechClient)
    assert isinstance(start_ms, int) and start_ms >= 0
    assert isinstance(duration_ms, int) and duration_ms >= 0
    assert audio_bytes_format is None or isinstance(audio_bytes_format, str)

    response = client.service_stub.GetAudio(
        GetAudioRequest(
            api_key=client.api_key,
            object_id=object_id,
            time_segment=GetAudioRequest.TimeSegment(
                start_ms=start_ms,
                duration_ms=duration_ms
            ),
            audio_bytes_format=audio_bytes_format
        )
    )
    return response


def get_audio_segment_by_token(
    object_id: str,
    client: SpeechClient,
    token_start: int,
    token_end: int,
    audio_bytes_format: Optional[str] = None
) -> GetAudioResponse:
    assert isinstance(object_id, str) and len(object_id) > 0
    assert isinstance(client, SpeechClient)
    assert isinstance(token_start, int) and token_start >= 0
    assert isinstance(token_end, int) and token_end >= 0
    assert audio_bytes_format is None or isinstance(audio_bytes_format, str)

    response = client.service_stub.GetAudio(
        GetAudioRequest(
            api_key=client.api_key,
            object_id=object_id,
            token_segment=GetAudioRequest.TokenSegment(
                token_start=token_start,
                token_end=token_end
            ),
            audio_bytes_format=audio_bytes_format
        )
    )
    return response