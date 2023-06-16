from datetime import datetime, timezone

from google.protobuf.timestamp_pb2 import Timestamp


def timestamp_from_datetime(dt: datetime) -> Timestamp:
    ts = Timestamp()
    ts.FromDatetime(dt)
    return ts


def timestamp_to_datetime(ts: Timestamp) -> datetime:
    return ts.ToDatetime(tzinfo=timezone.utc)
