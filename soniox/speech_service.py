from typing import Iterable, List, Optional
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
TranscribeMeetingConfig = speech_service_pb2.TranscribeMeetingConfig
TranscribeMeetingRequest = speech_service_pb2.TranscribeMeetingRequest
TranscribeMeetingResponse = speech_service_pb2.TranscribeMeetingResponse
TranscribeAsyncFileStatus = speech_service_pb2.TranscribeAsyncFileStatus

SpeechServiceStub = speech_service_pb2_grpc.SpeechServiceStub

_CERTS_FILE = os.path.realpath(os.path.join(os.path.dirname(__file__), "roots.pem"))
_API_HOST = ""
_API_KEY = ""
_DEFAULT_API_HOST = "https://api.soniox.com:443"


with open(_CERTS_FILE, "rb") as fh:
    _CREDENTIALS = grpc.ssl_channel_credentials(fh.read())


def set_api_host(api_host: str) -> None:
    assert isinstance(api_host, str)
    global _API_HOST
    _API_HOST = api_host


def get_api_host(api_host: Optional[str]) -> str:
    if api_host is not None and api_host != "":
        return api_host
    api_host = _API_HOST
    if api_host == "":
        api_host = os.getenv("SONIOX_API_HOST", default="")
    if api_host == "":
        api_host = _DEFAULT_API_HOST
    return api_host


def set_api_key(api_key: str) -> None:
    assert isinstance(api_key, str)
    global _API_KEY
    _API_KEY = api_key


def get_api_key(api_key: Optional[str]) -> str:
    if api_key is not None and api_key != "":
        return api_key
    api_key = _API_KEY
    if api_key == "<YOUR-API-KEY>":
        api_key = ""
    if api_key == "":
        api_key = os.getenv("SONIOX_API_KEY", default="")
    if api_key == "":
        raise Exception("Soniox API key not set. Please set it using soniox.service.set_api_key().")
    return api_key


def create_channel(api_host: Optional[str]) -> grpc.Channel:
    api_host = get_api_host(api_host)

    if api_host.startswith("http://"):
        return grpc.insecure_channel(api_host[7:])
    elif api_host.startswith("https://"):
        return grpc.secure_channel(api_host[8:], _CREDENTIALS)
    else:
        return grpc.insecure_channel(api_host)


class Client:
    def __init__(self, api_host: Optional[str] = None, api_key: Optional[str] = None) -> None:
        self._channel = create_channel(api_host)
        try:
            self._client = SpeechServiceStub(self._channel)
            self._api_key = get_api_key(api_key)
        except:
            self._channel.close()
            raise

    def close(self) -> None:
        self._channel.close()

    def __enter__(self) -> "Client":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()

    @property
    def service_stub(self) -> SpeechServiceStub:
        return self._client

    @property
    def api_key(self) -> str:
        return self._api_key

    def Transcribe(self, config: TranscribeConfig, audio: bytes) -> Result:
        assert isinstance(config, TranscribeConfig)
        assert isinstance(audio, bytes)

        request = speech_service_pb2.TranscribeRequest()
        request.api_key = self.api_key
        request.config.CopyFrom(config)
        request.audio = audio

        response = self._client.Transcribe(request)

        return response.result

    def TranscribeStream(
        self, config: TranscribeStreamConfig, iter_audio: Iterable[bytes]
    ) -> Iterable[Result]:
        assert isinstance(config, TranscribeStreamConfig)

        # If the request iterator throws an exception, gRPC throws its own exception
        # that does not have the original exception as the cause, which means one does
        # not see what the actual problem was. We fix this by remembering an exception
        # thrown from the request iterator and attaching it as the cause of the gRPC
        # exception below.
        iter_exception = None

        def iter_requests():
            nonlocal iter_exception

            try:
                request = speech_service_pb2.TranscribeStreamRequest()
                request.api_key = self.api_key
                request.config.CopyFrom(config)
                yield request

                for audio in iter_audio:
                    assert isinstance(audio, bytes)
                    request = speech_service_pb2.TranscribeStreamRequest()
                    request.audio = audio
                    yield request

            except Exception as e:
                iter_exception = e
                raise

        try:
            responses = self._client.TranscribeStream(iter_requests())

            for response in responses:
                if response.HasField("result"):
                    yield response.result

        except Exception as e:
            if iter_exception is not None:
                raise e from iter_exception
            raise

    def TranscribeMeeting(
        self, config: TranscribeMeetingConfig, iter_requests: Iterable[TranscribeMeetingRequest]
    ) -> Iterable[TranscribeMeetingResponse]:
        assert isinstance(config, TranscribeMeetingConfig)

        iter_exception = None

        def local_iter_requests():
            nonlocal iter_exception

            try:
                request = TranscribeMeetingRequest()
                request.api_key = self.api_key
                request.config.CopyFrom(config)
                request.seq_num = -1
                request.stream_id = 0
                yield request

                for request in iter_requests:
                    assert isinstance(request, TranscribeMeetingRequest)
                    yield request

            except Exception as e:
                iter_exception = e
                raise

        try:
            responses = self._client.TranscribeMeeting(local_iter_requests())

            first = True
            for response in responses:
                if not (first and response.seq_num == -1 and response.stream_id == 0):
                    yield response
                first = False

        except Exception as e:
            if iter_exception is not None:
                raise e from iter_exception
            raise

    def TranscribeAsync(self, reference_name: str, iter_audio: Iterable[bytes]) -> str:
        assert isinstance(reference_name, str)

        # See TranscribeStream for an explanation.
        iter_exception = None

        def iter_requests():
            nonlocal iter_exception

            try:
                request = speech_service_pb2.TranscribeAsyncRequest()
                request.api_key = self.api_key
                request.reference_name = reference_name
                yield request

                for audio in iter_audio:
                    assert isinstance(audio, bytes)
                    request = speech_service_pb2.TranscribeAsyncRequest()
                    request.audio = audio
                    yield request

            except Exception as e:
                iter_exception = e
                raise

        try:
            response = self._client.TranscribeAsync(iter_requests())
        except Exception as e:
            if iter_exception is not None:
                raise e from iter_exception
            raise

        return response.file_id

    def GetTranscribeAsyncFileStatus(self, file_id: str) -> TranscribeAsyncFileStatus:
        assert isinstance(file_id, str)
        assert file_id != ""

        request = speech_service_pb2.GetTranscribeAsyncStatusRequest()
        request.api_key = self.api_key
        request.file_id = file_id

        response = self._client.GetTranscribeAsyncStatus(request)

        if len(response.files) != 1:
            raise Exception(f"Unexpected number of files returned.")

        return response.files[0]

    def GetTranscribeAsyncAllFilesStatus(self) -> List[TranscribeAsyncFileStatus]:
        request = speech_service_pb2.GetTranscribeAsyncStatusRequest()
        request.api_key = self.api_key

        response = self._client.GetTranscribeAsyncStatus(request)

        return list(response.files)

    def GetTranscribeAsyncResult(self, file_id: str) -> Result:
        assert isinstance(file_id, str)
        assert file_id != ""

        request = speech_service_pb2.GetTranscribeAsyncResultRequest()
        request.api_key = self.api_key
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
        request.api_key = self.api_key
        request.file_id = file_id

        self._client.DeleteTranscribeAsyncFile(request)


def update_result(result: Result, new_result: Result) -> None:
    i = len(result.words)
    while i > 0 and not result.words[i - 1].is_final:
        i -= 1
    del result.words[i:]
    result.words.extend(new_result.words)
    result.final_proc_time_ms = new_result.final_proc_time_ms
    result.total_proc_time_ms = new_result.total_proc_time_ms
    del result.speakers[:]
    result.speakers.extend(new_result.speakers)


def merge_results(results: Iterable[Result]) -> Result:
    result = Result()
    for new_result in results:
        update_result(result, new_result)
    return result
