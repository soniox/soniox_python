# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from soniox import speech_service_pb2 as soniox_dot_speech__service__pb2


class SpeechServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Transcribe = channel.unary_unary(
                '/soniox.speech_service.SpeechService/Transcribe',
                request_serializer=soniox_dot_speech__service__pb2.TranscribeRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.TranscribeResponse.FromString,
                )
        self.TranscribeStream = channel.stream_stream(
                '/soniox.speech_service.SpeechService/TranscribeStream',
                request_serializer=soniox_dot_speech__service__pb2.TranscribeStreamRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.TranscribeStreamResponse.FromString,
                )
        self.TranscribeMeeting = channel.stream_stream(
                '/soniox.speech_service.SpeechService/TranscribeMeeting',
                request_serializer=soniox_dot_speech__service__pb2.TranscribeMeetingRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.TranscribeMeetingResponse.FromString,
                )
        self.TranscribeAsync = channel.stream_unary(
                '/soniox.speech_service.SpeechService/TranscribeAsync',
                request_serializer=soniox_dot_speech__service__pb2.TranscribeAsyncRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.TranscribeAsyncResponse.FromString,
                )
        self.GetTranscribeAsyncStatus = channel.unary_unary(
                '/soniox.speech_service.SpeechService/GetTranscribeAsyncStatus',
                request_serializer=soniox_dot_speech__service__pb2.GetTranscribeAsyncStatusRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.GetTranscribeAsyncStatusResponse.FromString,
                )
        self.GetTranscribeAsyncResult = channel.unary_stream(
                '/soniox.speech_service.SpeechService/GetTranscribeAsyncResult',
                request_serializer=soniox_dot_speech__service__pb2.GetTranscribeAsyncResultRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.GetTranscribeAsyncResultResponse.FromString,
                )
        self.DeleteTranscribeAsyncFile = channel.unary_unary(
                '/soniox.speech_service.SpeechService/DeleteTranscribeAsyncFile',
                request_serializer=soniox_dot_speech__service__pb2.DeleteTranscribeAsyncFileRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.DeleteTranscribeAsyncFileResponse.FromString,
                )
        self.CreateSpeechContext = channel.unary_unary(
                '/soniox.speech_service.SpeechService/CreateSpeechContext',
                request_serializer=soniox_dot_speech__service__pb2.CreateSpeechContextRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.CreateSpeechContextResponse.FromString,
                )
        self.DeleteSpeechContext = channel.unary_unary(
                '/soniox.speech_service.SpeechService/DeleteSpeechContext',
                request_serializer=soniox_dot_speech__service__pb2.DeleteSpeechContextRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.DeleteSpeechContextResponse.FromString,
                )
        self.ListSpeechContextNames = channel.unary_unary(
                '/soniox.speech_service.SpeechService/ListSpeechContextNames',
                request_serializer=soniox_dot_speech__service__pb2.ListSpeechContextNamesRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.ListSpeechContextNamesResponse.FromString,
                )
        self.GetSpeechContext = channel.unary_unary(
                '/soniox.speech_service.SpeechService/GetSpeechContext',
                request_serializer=soniox_dot_speech__service__pb2.GetSpeechContextRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.GetSpeechContextResponse.FromString,
                )
        self.UpdateSpeechContext = channel.unary_unary(
                '/soniox.speech_service.SpeechService/UpdateSpeechContext',
                request_serializer=soniox_dot_speech__service__pb2.UpdateSpeechContextRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.UpdateSpeechContextResponse.FromString,
                )
        self.AddSpeaker = channel.unary_unary(
                '/soniox.speech_service.SpeechService/AddSpeaker',
                request_serializer=soniox_dot_speech__service__pb2.AddSpeakerRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.AddSpeakerResponse.FromString,
                )
        self.GetSpeaker = channel.unary_unary(
                '/soniox.speech_service.SpeechService/GetSpeaker',
                request_serializer=soniox_dot_speech__service__pb2.GetSpeakerRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.GetSpeakerResponse.FromString,
                )
        self.RemoveSpeaker = channel.unary_unary(
                '/soniox.speech_service.SpeechService/RemoveSpeaker',
                request_serializer=soniox_dot_speech__service__pb2.RemoveSpeakerRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.RemoveSpeakerResponse.FromString,
                )
        self.ListSpeakers = channel.unary_unary(
                '/soniox.speech_service.SpeechService/ListSpeakers',
                request_serializer=soniox_dot_speech__service__pb2.ListSpeakersRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.ListSpeakersResponse.FromString,
                )
        self.AddSpeakerAudio = channel.unary_unary(
                '/soniox.speech_service.SpeechService/AddSpeakerAudio',
                request_serializer=soniox_dot_speech__service__pb2.AddSpeakerAudioRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.AddSpeakerAudioResponse.FromString,
                )
        self.GetSpeakerAudio = channel.unary_unary(
                '/soniox.speech_service.SpeechService/GetSpeakerAudio',
                request_serializer=soniox_dot_speech__service__pb2.GetSpeakerAudioRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.GetSpeakerAudioResponse.FromString,
                )
        self.RemoveSpeakerAudio = channel.unary_unary(
                '/soniox.speech_service.SpeechService/RemoveSpeakerAudio',
                request_serializer=soniox_dot_speech__service__pb2.RemoveSpeakerAudioRequest.SerializeToString,
                response_deserializer=soniox_dot_speech__service__pb2.RemoveSpeakerAudioResponse.FromString,
                )


class SpeechServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Transcribe(self, request, context):
        """Synchronous transcription
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TranscribeStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TranscribeMeeting(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TranscribeAsync(self, request_iterator, context):
        """Asynchronous transcription
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTranscribeAsyncStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTranscribeAsyncResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTranscribeAsyncFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSpeechContext(self, request, context):
        """Speech context
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSpeechContext(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSpeechContextNames(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSpeechContext(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSpeechContext(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSpeaker(self, request, context):
        """Speaker AI
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSpeaker(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveSpeaker(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSpeakers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSpeakerAudio(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSpeakerAudio(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveSpeakerAudio(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SpeechServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Transcribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Transcribe,
                    request_deserializer=soniox_dot_speech__service__pb2.TranscribeRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.TranscribeResponse.SerializeToString,
            ),
            'TranscribeStream': grpc.stream_stream_rpc_method_handler(
                    servicer.TranscribeStream,
                    request_deserializer=soniox_dot_speech__service__pb2.TranscribeStreamRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.TranscribeStreamResponse.SerializeToString,
            ),
            'TranscribeMeeting': grpc.stream_stream_rpc_method_handler(
                    servicer.TranscribeMeeting,
                    request_deserializer=soniox_dot_speech__service__pb2.TranscribeMeetingRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.TranscribeMeetingResponse.SerializeToString,
            ),
            'TranscribeAsync': grpc.stream_unary_rpc_method_handler(
                    servicer.TranscribeAsync,
                    request_deserializer=soniox_dot_speech__service__pb2.TranscribeAsyncRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.TranscribeAsyncResponse.SerializeToString,
            ),
            'GetTranscribeAsyncStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTranscribeAsyncStatus,
                    request_deserializer=soniox_dot_speech__service__pb2.GetTranscribeAsyncStatusRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.GetTranscribeAsyncStatusResponse.SerializeToString,
            ),
            'GetTranscribeAsyncResult': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTranscribeAsyncResult,
                    request_deserializer=soniox_dot_speech__service__pb2.GetTranscribeAsyncResultRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.GetTranscribeAsyncResultResponse.SerializeToString,
            ),
            'DeleteTranscribeAsyncFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTranscribeAsyncFile,
                    request_deserializer=soniox_dot_speech__service__pb2.DeleteTranscribeAsyncFileRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.DeleteTranscribeAsyncFileResponse.SerializeToString,
            ),
            'CreateSpeechContext': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateSpeechContext,
                    request_deserializer=soniox_dot_speech__service__pb2.CreateSpeechContextRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.CreateSpeechContextResponse.SerializeToString,
            ),
            'DeleteSpeechContext': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSpeechContext,
                    request_deserializer=soniox_dot_speech__service__pb2.DeleteSpeechContextRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.DeleteSpeechContextResponse.SerializeToString,
            ),
            'ListSpeechContextNames': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSpeechContextNames,
                    request_deserializer=soniox_dot_speech__service__pb2.ListSpeechContextNamesRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.ListSpeechContextNamesResponse.SerializeToString,
            ),
            'GetSpeechContext': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSpeechContext,
                    request_deserializer=soniox_dot_speech__service__pb2.GetSpeechContextRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.GetSpeechContextResponse.SerializeToString,
            ),
            'UpdateSpeechContext': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSpeechContext,
                    request_deserializer=soniox_dot_speech__service__pb2.UpdateSpeechContextRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.UpdateSpeechContextResponse.SerializeToString,
            ),
            'AddSpeaker': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSpeaker,
                    request_deserializer=soniox_dot_speech__service__pb2.AddSpeakerRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.AddSpeakerResponse.SerializeToString,
            ),
            'GetSpeaker': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSpeaker,
                    request_deserializer=soniox_dot_speech__service__pb2.GetSpeakerRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.GetSpeakerResponse.SerializeToString,
            ),
            'RemoveSpeaker': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveSpeaker,
                    request_deserializer=soniox_dot_speech__service__pb2.RemoveSpeakerRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.RemoveSpeakerResponse.SerializeToString,
            ),
            'ListSpeakers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSpeakers,
                    request_deserializer=soniox_dot_speech__service__pb2.ListSpeakersRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.ListSpeakersResponse.SerializeToString,
            ),
            'AddSpeakerAudio': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSpeakerAudio,
                    request_deserializer=soniox_dot_speech__service__pb2.AddSpeakerAudioRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.AddSpeakerAudioResponse.SerializeToString,
            ),
            'GetSpeakerAudio': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSpeakerAudio,
                    request_deserializer=soniox_dot_speech__service__pb2.GetSpeakerAudioRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.GetSpeakerAudioResponse.SerializeToString,
            ),
            'RemoveSpeakerAudio': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveSpeakerAudio,
                    request_deserializer=soniox_dot_speech__service__pb2.RemoveSpeakerAudioRequest.FromString,
                    response_serializer=soniox_dot_speech__service__pb2.RemoveSpeakerAudioResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'soniox.speech_service.SpeechService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SpeechService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Transcribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/Transcribe',
            soniox_dot_speech__service__pb2.TranscribeRequest.SerializeToString,
            soniox_dot_speech__service__pb2.TranscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TranscribeStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/soniox.speech_service.SpeechService/TranscribeStream',
            soniox_dot_speech__service__pb2.TranscribeStreamRequest.SerializeToString,
            soniox_dot_speech__service__pb2.TranscribeStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TranscribeMeeting(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/soniox.speech_service.SpeechService/TranscribeMeeting',
            soniox_dot_speech__service__pb2.TranscribeMeetingRequest.SerializeToString,
            soniox_dot_speech__service__pb2.TranscribeMeetingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TranscribeAsync(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/soniox.speech_service.SpeechService/TranscribeAsync',
            soniox_dot_speech__service__pb2.TranscribeAsyncRequest.SerializeToString,
            soniox_dot_speech__service__pb2.TranscribeAsyncResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTranscribeAsyncStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/GetTranscribeAsyncStatus',
            soniox_dot_speech__service__pb2.GetTranscribeAsyncStatusRequest.SerializeToString,
            soniox_dot_speech__service__pb2.GetTranscribeAsyncStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTranscribeAsyncResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/soniox.speech_service.SpeechService/GetTranscribeAsyncResult',
            soniox_dot_speech__service__pb2.GetTranscribeAsyncResultRequest.SerializeToString,
            soniox_dot_speech__service__pb2.GetTranscribeAsyncResultResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTranscribeAsyncFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/DeleteTranscribeAsyncFile',
            soniox_dot_speech__service__pb2.DeleteTranscribeAsyncFileRequest.SerializeToString,
            soniox_dot_speech__service__pb2.DeleteTranscribeAsyncFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateSpeechContext(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/CreateSpeechContext',
            soniox_dot_speech__service__pb2.CreateSpeechContextRequest.SerializeToString,
            soniox_dot_speech__service__pb2.CreateSpeechContextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSpeechContext(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/DeleteSpeechContext',
            soniox_dot_speech__service__pb2.DeleteSpeechContextRequest.SerializeToString,
            soniox_dot_speech__service__pb2.DeleteSpeechContextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSpeechContextNames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/ListSpeechContextNames',
            soniox_dot_speech__service__pb2.ListSpeechContextNamesRequest.SerializeToString,
            soniox_dot_speech__service__pb2.ListSpeechContextNamesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSpeechContext(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/GetSpeechContext',
            soniox_dot_speech__service__pb2.GetSpeechContextRequest.SerializeToString,
            soniox_dot_speech__service__pb2.GetSpeechContextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSpeechContext(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/UpdateSpeechContext',
            soniox_dot_speech__service__pb2.UpdateSpeechContextRequest.SerializeToString,
            soniox_dot_speech__service__pb2.UpdateSpeechContextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSpeaker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/AddSpeaker',
            soniox_dot_speech__service__pb2.AddSpeakerRequest.SerializeToString,
            soniox_dot_speech__service__pb2.AddSpeakerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSpeaker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/GetSpeaker',
            soniox_dot_speech__service__pb2.GetSpeakerRequest.SerializeToString,
            soniox_dot_speech__service__pb2.GetSpeakerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveSpeaker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/RemoveSpeaker',
            soniox_dot_speech__service__pb2.RemoveSpeakerRequest.SerializeToString,
            soniox_dot_speech__service__pb2.RemoveSpeakerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSpeakers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/ListSpeakers',
            soniox_dot_speech__service__pb2.ListSpeakersRequest.SerializeToString,
            soniox_dot_speech__service__pb2.ListSpeakersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSpeakerAudio(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/AddSpeakerAudio',
            soniox_dot_speech__service__pb2.AddSpeakerAudioRequest.SerializeToString,
            soniox_dot_speech__service__pb2.AddSpeakerAudioResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSpeakerAudio(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/GetSpeakerAudio',
            soniox_dot_speech__service__pb2.GetSpeakerAudioRequest.SerializeToString,
            soniox_dot_speech__service__pb2.GetSpeakerAudioResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveSpeakerAudio(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/soniox.speech_service.SpeechService/RemoveSpeakerAudio',
            soniox_dot_speech__service__pb2.RemoveSpeakerAudioRequest.SerializeToString,
            soniox_dot_speech__service__pb2.RemoveSpeakerAudioResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
