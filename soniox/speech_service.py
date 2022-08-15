from typing import Iterable, List, Optional, Union, Dict
import os
import grpc
import soniox.speech_service_pb2 as speech_service_pb2
import soniox.speech_service_pb2_grpc as speech_service_pb2_grpc

SpeechContext = speech_service_pb2.SpeechContext
SpeechContextEntry = speech_service_pb2.SpeechContextEntry
Result = speech_service_pb2.Result
Word = speech_service_pb2.Word
TranscriptionConfig = speech_service_pb2.TranscriptionConfig
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

    def Transcribe(self, config: TranscriptionConfig, audio: bytes) -> Union[Result, List[Result]]:
        assert isinstance(config, TranscriptionConfig)
        assert isinstance(audio, bytes)

        request = speech_service_pb2.TranscribeRequest()
        request.api_key = self.api_key
        request.config.CopyFrom(config)
        request.audio = audio

        response = self._client.Transcribe(request)

        if not config.enable_separate_recognition_per_channel:
            assert response.HasField("result")
            assert len(response.channel_results) == 0
            return response.result
        else:
            assert not response.HasField("result")
            assert len(response.channel_results) > 0
            return list(response.channel_results)

    def TranscribeStream(
        self, config: TranscriptionConfig, iter_audio: Iterable[bytes]
    ) -> Iterable[Result]:
        assert isinstance(config, TranscriptionConfig)

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

    def TranscribeStreamFile(
        self, config: TranscriptionConfig, iter_audio: Iterable[bytes]
    ) -> Union[Result, List[Result]]:
        assert not config.include_nonfinal

        if not config.enable_separate_recognition_per_channel:
            got_result = False
            result = Result()

            for resp_result in self.TranscribeStream(config, iter_audio):
                got_result = True
                update_result(result, resp_result)

            assert got_result
            return result
        else:
            channel_results: Dict[int, Result] = {}

            for resp_result in self.TranscribeStream(config, iter_audio):
                channel = resp_result.channel
                if channel not in channel_results:
                    channel_results[channel] = Result(channel=channel)
                update_result(channel_results[channel], resp_result)

            assert len(channel_results) > 0
            channels = sorted(channel_results.keys())
            assert channels == list(range(len(channel_results)))
            return [channel_results[channel] for channel in channels]

    def TranscribeMeeting(
        self, config: TranscriptionConfig, iter_requests: Iterable[TranscribeMeetingRequest]
    ) -> Iterable[TranscribeMeetingResponse]:
        assert isinstance(config, TranscriptionConfig)

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

    def TranscribeAsync(
        self, reference_name: str, iter_audio: Iterable[bytes], config: TranscriptionConfig
    ) -> str:
        assert isinstance(reference_name, str)

        # See TranscribeStream for an explanation.
        iter_exception = None

        def iter_requests():
            nonlocal iter_exception

            try:
                request = speech_service_pb2.TranscribeAsyncRequest()
                request.api_key = self.api_key
                request.reference_name = reference_name
                request.config.CopyFrom(config)
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

    def GetTranscribeAsyncResult(self, file_id: str) -> Union[Result, List[Result]]:
        assert isinstance(file_id, str)
        assert file_id != ""

        request = speech_service_pb2.GetTranscribeAsyncResultRequest()
        request.api_key = self.api_key
        request.file_id = file_id

        got_responses = False
        result: Optional[Result] = None
        channel_results: Optional[Dict[int, Result]] = None

        for response in self._client.GetTranscribeAsyncResult(request):
            if not got_responses:
                if not response.separate_recognition_per_channel:
                    result = Result()
                else:
                    channel_results = {}
                got_responses = True

            assert response.HasField("result")

            if not response.separate_recognition_per_channel:
                assert result is not None
                update_result(result, response.result)
            else:
                assert channel_results is not None
                channel = response.result.channel
                if channel not in channel_results:
                    channel_results[channel] = Result(channel=channel)
                update_result(channel_results[channel], response.result)

        assert got_responses
        if result is not None:
            return result
        else:
            assert channel_results is not None
            assert len(channel_results) > 0
            channels = sorted(channel_results.keys())
            assert channels == list(range(len(channel_results)))
            return [channel_results[channel] for channel in channels]

    def DeleteTranscribeAsyncFile(self, file_id: str) -> None:
        assert isinstance(file_id, str)
        assert file_id != ""

        request = speech_service_pb2.DeleteTranscribeAsyncFileRequest()
        request.api_key = self.api_key
        request.file_id = file_id

        self._client.DeleteTranscribeAsyncFile(request)


def update_result(result: Result, new_result: Result) -> None:
    assert result.channel == new_result.channel
    i = len(result.words)
    while i > 0 and not result.words[i - 1].is_final:
        i -= 1
    del result.words[i:]
    result.words.extend(new_result.words)
    result.final_proc_time_ms = new_result.final_proc_time_ms
    result.total_proc_time_ms = new_result.total_proc_time_ms
    del result.speakers[:]
    result.speakers.extend(new_result.speakers)
