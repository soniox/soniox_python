from typing import Iterable, List
import os
import grpc
import soniox.speech_service_pb2 as speech_service_pb2
import soniox.speech_service_pb2_grpc as speech_service_pb2_grpc

SpeechContext = speech_service_pb2.SpeechContext
SpeechContextEntry = speech_service_pb2.SpeechContextEntry
Result = speech_service_pb2.Result
Word = speech_service_pb2.Word
TranscribeConfig = speech_service_pb2.TranscribeConfig
TranscribeStreamConfig = speech_service_pb2.TranscribeStreamConfig
TranscribeAsyncFileStatus = speech_service_pb2.TranscribeAsyncFileStatus

SpeechServiceStub = speech_service_pb2_grpc.SpeechServiceStub

_CERTS_FILE = os.path.realpath(os.path.join(
    os.path.dirname(__file__), "roots.pem"))
_API_HOST = ""
_API_KEY = ""
_DEFAULT_API_HOST = "https://api.soniox.com:443"


with open(_CERTS_FILE, "rb") as fh:
    _CREDENTIALS = grpc.ssl_channel_credentials(fh.read())


def set_api_host(api_host: str) -> None:
    assert isinstance(api_host, str)
    global _API_HOST
    _API_HOST = api_host


def set_api_key(api_key: str) -> None:
    assert isinstance(api_key, str)
    global _API_KEY
    _API_KEY = api_key


def get_api_key() -> str:
    api_key = _API_KEY
    if api_key == "<YOUR-API-KEY>":
        api_key = ""
    if len(api_key) == 0:
        api_key = os.getenv("SONIOX_API_KEY", default="")
    if len(api_key) == 0:
        raise Exception(
            "Soniox API key not set. Please set it using soniox.service.set_api_key().")
    return api_key


def create_channel() -> grpc.Channel:
    api_host = _API_HOST
    if len(api_host) == 0:
        api_host = os.getenv("SONIOX_API_HOST", default="")
    if len(api_host) == 0:
        api_host = _DEFAULT_API_HOST
    if api_host.startswith("http://"):
        return grpc.insecure_channel(api_host[7:])
    elif api_host.startswith("https://"):
        return grpc.secure_channel(api_host[8:], _CREDENTIALS)
    else:
        return grpc.insecure_channel(api_host)


class Client:
    def __init__(self) -> None:
        self._channel = create_channel()
        self._channel.__enter__()
        self._client = SpeechServiceStub(self._channel)

    def __enter__(self) -> "Client":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self._channel.__exit__(exc_type, exc_value, traceback)

    @property
    def service_stub(self) -> SpeechServiceStub:
        return self._client

    def Transcribe(self, config: TranscribeConfig, audio: bytes) -> Result:
        assert isinstance(config, TranscribeConfig)
        assert isinstance(audio, bytes)

        request = speech_service_pb2.TranscribeRequest()
        request.api_key = get_api_key()
        request.config.CopyFrom(config)
        request.audio = audio

        response = self._client.Transcribe(request)

        return response.result

    def TranscribeStream(
        self, config: TranscribeStreamConfig, iter_audio: Iterable[bytes]
    ) -> Iterable[Result]:
        assert isinstance(config, TranscribeStreamConfig)

        def iter_requests():
            request = speech_service_pb2.TranscribeStreamRequest()
            request.api_key = get_api_key()
            request.config.CopyFrom(config)
            yield request

            for audio in iter_audio:
                assert isinstance(audio, bytes)
                request = speech_service_pb2.TranscribeStreamRequest()
                request.audio = audio
                yield request

        responses = self._client.TranscribeStream(iter_requests())

        for response in responses:
            if response.HasField("result"):
                yield response.result

    def TranscribeAsync(self, reference_name: str, iter_audio: Iterable[bytes]) -> str:
        assert isinstance(reference_name, str)

        def iter_requests():
            request = speech_service_pb2.TranscribeAsyncRequest()
            request.api_key = get_api_key()
            request.reference_name = reference_name
            yield request

            for audio in iter_audio:
                assert isinstance(audio, bytes)
                request = speech_service_pb2.TranscribeAsyncRequest()
                request.audio = audio
                yield request

        response = self._client.TranscribeAsync(iter_requests())

        return response.file_id

    def GetTranscribeAsyncFileStatus(self, file_id: str) -> TranscribeAsyncFileStatus:
        assert isinstance(file_id, str)
        assert file_id != ""

        request = speech_service_pb2.GetTranscribeAsyncStatusRequest()
        request.api_key = get_api_key()
        request.file_id = file_id

        response = self._client.GetTranscribeAsyncStatus(request)

        if len(response.files) != 1:
            raise Exception(f"Unexpected number of files returned.")

        return response.files[0]

    def GetTranscribeAsyncAllFilesStatus(self) -> List[TranscribeAsyncFileStatus]:
        request = speech_service_pb2.GetTranscribeAsyncStatusRequest()
        request.api_key = get_api_key()

        response = self._client.GetTranscribeAsyncStatus(request)

        return list(response.files)

    def GetTranscribeAsyncResult(self, file_id: str) -> Result:
        assert isinstance(file_id, str)
        assert file_id != ""

        request = speech_service_pb2.GetTranscribeAsyncResultRequest()
        request.api_key = get_api_key()
        request.file_id = file_id

        got_responses = False
        result = Result()

        for response in self._client.GetTranscribeAsyncResult(request):
            got_responses = True
            result.words.extend(response.result.words)
            result.final_proc_time_ms = response.result.final_proc_time_ms
            result.total_proc_time_ms = response.result.total_proc_time_ms

        if not got_responses:
            raise Exception("No responses received.")

        return result

    def DeleteTranscribeAsyncFile(self, file_id: str) -> None:
        assert isinstance(file_id, str)
        assert file_id != ""

        request = speech_service_pb2.DeleteTranscribeAsyncFileRequest()
        request.api_key = get_api_key()
        request.file_id = file_id

        self._client.DeleteTranscribeAsyncFile(request)
