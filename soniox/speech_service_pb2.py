# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: soniox/speech_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bsoniox/speech_service.proto\x12\x15soniox.speech_service\x1a\x1fgoogle/protobuf/timestamp.proto\"l\n\x11TranscribeRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x37\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\'.soniox.speech_service.TranscribeConfig\x12\r\n\x05\x61udio\x18\x03 \x01(\x0c\"\xd9\x03\n\x10TranscribeConfig\x12\x14\n\x0c\x61udio_format\x18\x01 \x01(\t\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05\x12\x1a\n\x12num_audio_channels\x18\x03 \x01(\x05\x12<\n\x0espeech_context\x18\x04 \x01(\x0b\x32$.soniox.speech_service.SpeechContext\x12\x1f\n\x17\x65nable_profanity_filter\x18\x08 \x01(\x08\x12 \n\x18profanity_filter_phrases\x18\x12 \x03(\t\x12)\n!enable_global_speaker_diarization\x18\x0c \x01(\x08\x12,\n$enable_streaming_speaker_diarization\x18\x05 \x01(\x08\x12\x18\n\x10min_num_speakers\x18\r \x01(\x05\x12\x18\n\x10max_num_speakers\x18\x0e \x01(\x05\x12%\n\x1d\x65nable_speaker_identification\x18\x10 \x01(\x08\x12\x1a\n\x12\x63\x61nd_speaker_names\x18\x11 \x03(\t\x12\r\n\x05model\x18\n \x01(\t\x12\x18\n\x10\x65nable_dictation\x18\x0b \x01(\x08\"C\n\x12TranscribeResponse\x12-\n\x06result\x18\x01 \x01(\x0b\x32\x1d.soniox.speech_service.Result\"x\n\x17TranscribeStreamRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12=\n\x06\x63onfig\x18\x02 \x01(\x0b\x32-.soniox.speech_service.TranscribeStreamConfig\x12\r\n\x05\x61udio\x18\x03 \x01(\x0c\"\xf9\x03\n\x16TranscribeStreamConfig\x12\x14\n\x0c\x61udio_format\x18\x01 \x01(\t\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05\x12\x1a\n\x12num_audio_channels\x18\x03 \x01(\x05\x12\x18\n\x10include_nonfinal\x18\x05 \x01(\x08\x12<\n\x0espeech_context\x18\x04 \x01(\x0b\x32$.soniox.speech_service.SpeechContext\x12\x1f\n\x17\x65nable_profanity_filter\x18\t \x01(\x08\x12 \n\x18profanity_filter_phrases\x18\x13 \x03(\t\x12)\n!enable_global_speaker_diarization\x18\r \x01(\x08\x12,\n$enable_streaming_speaker_diarization\x18\x06 \x01(\x08\x12\x18\n\x10min_num_speakers\x18\x0e \x01(\x05\x12\x18\n\x10max_num_speakers\x18\x0f \x01(\x05\x12%\n\x1d\x65nable_speaker_identification\x18\x11 \x01(\x08\x12\x1a\n\x12\x63\x61nd_speaker_names\x18\x12 \x03(\t\x12\r\n\x05model\x18\x0b \x01(\t\x12\x18\n\x10\x65nable_dictation\x18\x0c \x01(\x08\"I\n\x18TranscribeStreamResponse\x12-\n\x06result\x18\x01 \x01(\x0b\x32\x1d.soniox.speech_service.Result\"\xd0\x01\n\x18TranscribeMeetingRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12>\n\x06\x63onfig\x18\x02 \x01(\x0b\x32..soniox.speech_service.TranscribeMeetingConfig\x12\x0f\n\x07seq_num\x18\x03 \x01(\x05\x12\x11\n\tstream_id\x18\x04 \x01(\x05\x12\x18\n\x10start_of_segment\x18\x05 \x01(\x08\x12\r\n\x05\x61udio\x18\x06 \x01(\x0c\x12\x16\n\x0e\x65nd_of_segment\x18\x07 \x01(\x08\"\x90\x02\n\x17TranscribeMeetingConfig\x12\x14\n\x0c\x61udio_format\x18\x01 \x01(\t\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05\x12\x1a\n\x12num_audio_channels\x18\x03 \x01(\x05\x12<\n\x0espeech_context\x18\x04 \x01(\x0b\x32$.soniox.speech_service.SpeechContext\x12\x1f\n\x17\x65nable_profanity_filter\x18\x05 \x01(\x08\x12 \n\x18profanity_filter_phrases\x18\n \x03(\t\x12\r\n\x05model\x18\x08 \x01(\t\x12\x18\n\x10\x65nable_dictation\x18\t \x01(\x08\"\xaf\x01\n\x19TranscribeMeetingResponse\x12\x0f\n\x07seq_num\x18\x01 \x01(\x05\x12\x11\n\tstream_id\x18\x02 \x01(\x05\x12\x18\n\x10start_of_segment\x18\x03 \x01(\x08\x12\x16\n\x0e\x65nd_of_segment\x18\x04 \x01(\x08\x12-\n\x06result\x18\x05 \x01(\x0b\x32\x1d.soniox.speech_service.Result\x12\r\n\x05\x65rror\x18\x06 \x01(\t\"P\n\x16TranscribeAsyncRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x16\n\x0ereference_name\x18\x03 \x01(\t\x12\r\n\x05\x61udio\x18\x04 \x01(\x0c\"*\n\x17TranscribeAsyncResponse\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\"C\n\x1fGetTranscribeAsyncStatusRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x0f\n\x07\x66ile_id\x18\x02 \x01(\t\"c\n GetTranscribeAsyncStatusResponse\x12?\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x30.soniox.speech_service.TranscribeAsyncFileStatus\"\x86\x01\n\x19TranscribeAsyncFileStatus\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\x12\x16\n\x0ereference_name\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x30\n\x0c\x63reated_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"C\n\x1fGetTranscribeAsyncResultRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x0f\n\x07\x66ile_id\x18\x02 \x01(\t\"Q\n GetTranscribeAsyncResultResponse\x12-\n\x06result\x18\x01 \x01(\x0b\x32\x1d.soniox.speech_service.Result\"D\n DeleteTranscribeAsyncFileRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x0f\n\x07\x66ile_id\x18\x02 \x01(\t\"#\n!DeleteTranscribeAsyncFileResponse\"\xa4\x01\n\x06Result\x12*\n\x05words\x18\x01 \x03(\x0b\x32\x1b.soniox.speech_service.Word\x12\x1a\n\x12\x66inal_proc_time_ms\x18\x02 \x01(\x05\x12\x1a\n\x12total_proc_time_ms\x18\x03 \x01(\x05\x12\x36\n\x08speakers\x18\x06 \x03(\x0b\x32$.soniox.speech_service.ResultSpeaker\"\x85\x01\n\x04Word\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x08start_ms\x18\x02 \x01(\x05\x12\x13\n\x0b\x64uration_ms\x18\x03 \x01(\x05\x12\x10\n\x08is_final\x18\x04 \x01(\x08\x12\x0f\n\x07speaker\x18\x05 \x01(\x05\x12\x11\n\torig_text\x18\x08 \x01(\t\x12\x12\n\nconfidence\x18\t \x01(\x01\".\n\rResultSpeaker\x12\x0f\n\x07speaker\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"Y\n\rSpeechContext\x12:\n\x07\x65ntries\x18\x01 \x03(\x0b\x32).soniox.speech_service.SpeechContextEntry\x12\x0c\n\x04name\x18\x02 \x01(\t\"4\n\x12SpeechContextEntry\x12\x0f\n\x07phrases\x18\x01 \x03(\t\x12\r\n\x05\x62oost\x18\x02 \x01(\x01\"k\n\x1a\x43reateSpeechContextRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12<\n\x0espeech_context\x18\x02 \x01(\x0b\x32$.soniox.speech_service.SpeechContext\"\x1d\n\x1b\x43reateSpeechContextResponse\";\n\x1a\x44\x65leteSpeechContextRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1d\n\x1b\x44\x65leteSpeechContextResponse\"0\n\x1dListSpeechContextNamesRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\"/\n\x1eListSpeechContextNamesResponse\x12\r\n\x05names\x18\x01 \x03(\t\"8\n\x17GetSpeechContextRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"X\n\x18GetSpeechContextResponse\x12<\n\x0espeech_context\x18\x01 \x01(\x0b\x32$.soniox.speech_service.SpeechContext\"k\n\x1aUpdateSpeechContextRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12<\n\x0espeech_context\x18\x02 \x01(\x0b\x32$.soniox.speech_service.SpeechContext\"\x1d\n\x1bUpdateSpeechContextResponse\"2\n\x11\x41\x64\x64SpeakerRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"O\n\x12\x41\x64\x64SpeakerResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x07\x63reated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"2\n\x11GetSpeakerRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x8f\x01\n\x12GetSpeakerResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x07\x63reated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12>\n\x06\x61udios\x18\x03 \x03(\x0b\x32..soniox.speech_service.GetSpeakerResponseAudio\"o\n\x17GetSpeakerResponseAudio\x12\x12\n\naudio_name\x18\x01 \x01(\t\x12+\n\x07\x63reated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64uration_ms\x18\x03 \x01(\x05\"5\n\x14RemoveSpeakerRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x17\n\x15RemoveSpeakerResponse\"&\n\x13ListSpeakersRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\"\\\n\x14ListSpeakersResponse\x12\x44\n\x08speakers\x18\x01 \x03(\x0b\x32\x32.soniox.speech_service.ListSpeakersResponseSpeaker\"l\n\x1bListSpeakersResponseSpeaker\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x07\x63reated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nnum_audios\x18\x03 \x01(\x05\"b\n\x16\x41\x64\x64SpeakerAudioRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x14\n\x0cspeaker_name\x18\x02 \x01(\t\x12\x12\n\naudio_name\x18\x03 \x01(\t\x12\r\n\x05\x61udio\x18\x04 \x01(\x0c\"\x85\x01\n\x17\x41\x64\x64SpeakerAudioResponse\x12\x14\n\x0cspeaker_name\x18\x01 \x01(\t\x12\x12\n\naudio_name\x18\x02 \x01(\t\x12+\n\x07\x63reated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64uration_ms\x18\x04 \x01(\x05\"S\n\x16GetSpeakerAudioRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x14\n\x0cspeaker_name\x18\x02 \x01(\t\x12\x12\n\naudio_name\x18\x03 \x01(\t\"\x94\x01\n\x17GetSpeakerAudioResponse\x12\x14\n\x0cspeaker_name\x18\x01 \x01(\t\x12\x12\n\naudio_name\x18\x02 \x01(\t\x12+\n\x07\x63reated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64uration_ms\x18\x04 \x01(\x05\x12\r\n\x05\x61udio\x18\x05 \x01(\x0c\"V\n\x19RemoveSpeakerAudioRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x14\n\x0cspeaker_name\x18\x02 \x01(\t\x12\x12\n\naudio_name\x18\x03 \x01(\t\"\x1c\n\x1aRemoveSpeakerAudioResponse2\xa1\x12\n\rSpeechService\x12\x63\n\nTranscribe\x12(.soniox.speech_service.TranscribeRequest\x1a).soniox.speech_service.TranscribeResponse\"\x00\x12y\n\x10TranscribeStream\x12..soniox.speech_service.TranscribeStreamRequest\x1a/.soniox.speech_service.TranscribeStreamResponse\"\x00(\x01\x30\x01\x12|\n\x11TranscribeMeeting\x12/.soniox.speech_service.TranscribeMeetingRequest\x1a\x30.soniox.speech_service.TranscribeMeetingResponse\"\x00(\x01\x30\x01\x12t\n\x0fTranscribeAsync\x12-.soniox.speech_service.TranscribeAsyncRequest\x1a..soniox.speech_service.TranscribeAsyncResponse\"\x00(\x01\x12\x8d\x01\n\x18GetTranscribeAsyncStatus\x12\x36.soniox.speech_service.GetTranscribeAsyncStatusRequest\x1a\x37.soniox.speech_service.GetTranscribeAsyncStatusResponse\"\x00\x12\x8f\x01\n\x18GetTranscribeAsyncResult\x12\x36.soniox.speech_service.GetTranscribeAsyncResultRequest\x1a\x37.soniox.speech_service.GetTranscribeAsyncResultResponse\"\x00\x30\x01\x12\x90\x01\n\x19\x44\x65leteTranscribeAsyncFile\x12\x37.soniox.speech_service.DeleteTranscribeAsyncFileRequest\x1a\x38.soniox.speech_service.DeleteTranscribeAsyncFileResponse\"\x00\x12~\n\x13\x43reateSpeechContext\x12\x31.soniox.speech_service.CreateSpeechContextRequest\x1a\x32.soniox.speech_service.CreateSpeechContextResponse\"\x00\x12~\n\x13\x44\x65leteSpeechContext\x12\x31.soniox.speech_service.DeleteSpeechContextRequest\x1a\x32.soniox.speech_service.DeleteSpeechContextResponse\"\x00\x12\x87\x01\n\x16ListSpeechContextNames\x12\x34.soniox.speech_service.ListSpeechContextNamesRequest\x1a\x35.soniox.speech_service.ListSpeechContextNamesResponse\"\x00\x12u\n\x10GetSpeechContext\x12..soniox.speech_service.GetSpeechContextRequest\x1a/.soniox.speech_service.GetSpeechContextResponse\"\x00\x12~\n\x13UpdateSpeechContext\x12\x31.soniox.speech_service.UpdateSpeechContextRequest\x1a\x32.soniox.speech_service.UpdateSpeechContextResponse\"\x00\x12\x63\n\nAddSpeaker\x12(.soniox.speech_service.AddSpeakerRequest\x1a).soniox.speech_service.AddSpeakerResponse\"\x00\x12\x63\n\nGetSpeaker\x12(.soniox.speech_service.GetSpeakerRequest\x1a).soniox.speech_service.GetSpeakerResponse\"\x00\x12l\n\rRemoveSpeaker\x12+.soniox.speech_service.RemoveSpeakerRequest\x1a,.soniox.speech_service.RemoveSpeakerResponse\"\x00\x12i\n\x0cListSpeakers\x12*.soniox.speech_service.ListSpeakersRequest\x1a+.soniox.speech_service.ListSpeakersResponse\"\x00\x12r\n\x0f\x41\x64\x64SpeakerAudio\x12-.soniox.speech_service.AddSpeakerAudioRequest\x1a..soniox.speech_service.AddSpeakerAudioResponse\"\x00\x12r\n\x0fGetSpeakerAudio\x12-.soniox.speech_service.GetSpeakerAudioRequest\x1a..soniox.speech_service.GetSpeakerAudioResponse\"\x00\x12{\n\x12RemoveSpeakerAudio\x12\x30.soniox.speech_service.RemoveSpeakerAudioRequest\x1a\x31.soniox.speech_service.RemoveSpeakerAudioResponse\"\x00\x62\x06proto3')



_TRANSCRIBEREQUEST = DESCRIPTOR.message_types_by_name['TranscribeRequest']
_TRANSCRIBECONFIG = DESCRIPTOR.message_types_by_name['TranscribeConfig']
_TRANSCRIBERESPONSE = DESCRIPTOR.message_types_by_name['TranscribeResponse']
_TRANSCRIBESTREAMREQUEST = DESCRIPTOR.message_types_by_name['TranscribeStreamRequest']
_TRANSCRIBESTREAMCONFIG = DESCRIPTOR.message_types_by_name['TranscribeStreamConfig']
_TRANSCRIBESTREAMRESPONSE = DESCRIPTOR.message_types_by_name['TranscribeStreamResponse']
_TRANSCRIBEMEETINGREQUEST = DESCRIPTOR.message_types_by_name['TranscribeMeetingRequest']
_TRANSCRIBEMEETINGCONFIG = DESCRIPTOR.message_types_by_name['TranscribeMeetingConfig']
_TRANSCRIBEMEETINGRESPONSE = DESCRIPTOR.message_types_by_name['TranscribeMeetingResponse']
_TRANSCRIBEASYNCREQUEST = DESCRIPTOR.message_types_by_name['TranscribeAsyncRequest']
_TRANSCRIBEASYNCRESPONSE = DESCRIPTOR.message_types_by_name['TranscribeAsyncResponse']
_GETTRANSCRIBEASYNCSTATUSREQUEST = DESCRIPTOR.message_types_by_name['GetTranscribeAsyncStatusRequest']
_GETTRANSCRIBEASYNCSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['GetTranscribeAsyncStatusResponse']
_TRANSCRIBEASYNCFILESTATUS = DESCRIPTOR.message_types_by_name['TranscribeAsyncFileStatus']
_GETTRANSCRIBEASYNCRESULTREQUEST = DESCRIPTOR.message_types_by_name['GetTranscribeAsyncResultRequest']
_GETTRANSCRIBEASYNCRESULTRESPONSE = DESCRIPTOR.message_types_by_name['GetTranscribeAsyncResultResponse']
_DELETETRANSCRIBEASYNCFILEREQUEST = DESCRIPTOR.message_types_by_name['DeleteTranscribeAsyncFileRequest']
_DELETETRANSCRIBEASYNCFILERESPONSE = DESCRIPTOR.message_types_by_name['DeleteTranscribeAsyncFileResponse']
_RESULT = DESCRIPTOR.message_types_by_name['Result']
_WORD = DESCRIPTOR.message_types_by_name['Word']
_RESULTSPEAKER = DESCRIPTOR.message_types_by_name['ResultSpeaker']
_SPEECHCONTEXT = DESCRIPTOR.message_types_by_name['SpeechContext']
_SPEECHCONTEXTENTRY = DESCRIPTOR.message_types_by_name['SpeechContextEntry']
_CREATESPEECHCONTEXTREQUEST = DESCRIPTOR.message_types_by_name['CreateSpeechContextRequest']
_CREATESPEECHCONTEXTRESPONSE = DESCRIPTOR.message_types_by_name['CreateSpeechContextResponse']
_DELETESPEECHCONTEXTREQUEST = DESCRIPTOR.message_types_by_name['DeleteSpeechContextRequest']
_DELETESPEECHCONTEXTRESPONSE = DESCRIPTOR.message_types_by_name['DeleteSpeechContextResponse']
_LISTSPEECHCONTEXTNAMESREQUEST = DESCRIPTOR.message_types_by_name['ListSpeechContextNamesRequest']
_LISTSPEECHCONTEXTNAMESRESPONSE = DESCRIPTOR.message_types_by_name['ListSpeechContextNamesResponse']
_GETSPEECHCONTEXTREQUEST = DESCRIPTOR.message_types_by_name['GetSpeechContextRequest']
_GETSPEECHCONTEXTRESPONSE = DESCRIPTOR.message_types_by_name['GetSpeechContextResponse']
_UPDATESPEECHCONTEXTREQUEST = DESCRIPTOR.message_types_by_name['UpdateSpeechContextRequest']
_UPDATESPEECHCONTEXTRESPONSE = DESCRIPTOR.message_types_by_name['UpdateSpeechContextResponse']
_ADDSPEAKERREQUEST = DESCRIPTOR.message_types_by_name['AddSpeakerRequest']
_ADDSPEAKERRESPONSE = DESCRIPTOR.message_types_by_name['AddSpeakerResponse']
_GETSPEAKERREQUEST = DESCRIPTOR.message_types_by_name['GetSpeakerRequest']
_GETSPEAKERRESPONSE = DESCRIPTOR.message_types_by_name['GetSpeakerResponse']
_GETSPEAKERRESPONSEAUDIO = DESCRIPTOR.message_types_by_name['GetSpeakerResponseAudio']
_REMOVESPEAKERREQUEST = DESCRIPTOR.message_types_by_name['RemoveSpeakerRequest']
_REMOVESPEAKERRESPONSE = DESCRIPTOR.message_types_by_name['RemoveSpeakerResponse']
_LISTSPEAKERSREQUEST = DESCRIPTOR.message_types_by_name['ListSpeakersRequest']
_LISTSPEAKERSRESPONSE = DESCRIPTOR.message_types_by_name['ListSpeakersResponse']
_LISTSPEAKERSRESPONSESPEAKER = DESCRIPTOR.message_types_by_name['ListSpeakersResponseSpeaker']
_ADDSPEAKERAUDIOREQUEST = DESCRIPTOR.message_types_by_name['AddSpeakerAudioRequest']
_ADDSPEAKERAUDIORESPONSE = DESCRIPTOR.message_types_by_name['AddSpeakerAudioResponse']
_GETSPEAKERAUDIOREQUEST = DESCRIPTOR.message_types_by_name['GetSpeakerAudioRequest']
_GETSPEAKERAUDIORESPONSE = DESCRIPTOR.message_types_by_name['GetSpeakerAudioResponse']
_REMOVESPEAKERAUDIOREQUEST = DESCRIPTOR.message_types_by_name['RemoveSpeakerAudioRequest']
_REMOVESPEAKERAUDIORESPONSE = DESCRIPTOR.message_types_by_name['RemoveSpeakerAudioResponse']
TranscribeRequest = _reflection.GeneratedProtocolMessageType('TranscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIBEREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.TranscribeRequest)
  })
_sym_db.RegisterMessage(TranscribeRequest)

TranscribeConfig = _reflection.GeneratedProtocolMessageType('TranscribeConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIBECONFIG,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.TranscribeConfig)
  })
_sym_db.RegisterMessage(TranscribeConfig)

TranscribeResponse = _reflection.GeneratedProtocolMessageType('TranscribeResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIBERESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.TranscribeResponse)
  })
_sym_db.RegisterMessage(TranscribeResponse)

TranscribeStreamRequest = _reflection.GeneratedProtocolMessageType('TranscribeStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIBESTREAMREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.TranscribeStreamRequest)
  })
_sym_db.RegisterMessage(TranscribeStreamRequest)

TranscribeStreamConfig = _reflection.GeneratedProtocolMessageType('TranscribeStreamConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIBESTREAMCONFIG,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.TranscribeStreamConfig)
  })
_sym_db.RegisterMessage(TranscribeStreamConfig)

TranscribeStreamResponse = _reflection.GeneratedProtocolMessageType('TranscribeStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIBESTREAMRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.TranscribeStreamResponse)
  })
_sym_db.RegisterMessage(TranscribeStreamResponse)

TranscribeMeetingRequest = _reflection.GeneratedProtocolMessageType('TranscribeMeetingRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIBEMEETINGREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.TranscribeMeetingRequest)
  })
_sym_db.RegisterMessage(TranscribeMeetingRequest)

TranscribeMeetingConfig = _reflection.GeneratedProtocolMessageType('TranscribeMeetingConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIBEMEETINGCONFIG,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.TranscribeMeetingConfig)
  })
_sym_db.RegisterMessage(TranscribeMeetingConfig)

TranscribeMeetingResponse = _reflection.GeneratedProtocolMessageType('TranscribeMeetingResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIBEMEETINGRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.TranscribeMeetingResponse)
  })
_sym_db.RegisterMessage(TranscribeMeetingResponse)

TranscribeAsyncRequest = _reflection.GeneratedProtocolMessageType('TranscribeAsyncRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIBEASYNCREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.TranscribeAsyncRequest)
  })
_sym_db.RegisterMessage(TranscribeAsyncRequest)

TranscribeAsyncResponse = _reflection.GeneratedProtocolMessageType('TranscribeAsyncResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIBEASYNCRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.TranscribeAsyncResponse)
  })
_sym_db.RegisterMessage(TranscribeAsyncResponse)

GetTranscribeAsyncStatusRequest = _reflection.GeneratedProtocolMessageType('GetTranscribeAsyncStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSCRIBEASYNCSTATUSREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.GetTranscribeAsyncStatusRequest)
  })
_sym_db.RegisterMessage(GetTranscribeAsyncStatusRequest)

GetTranscribeAsyncStatusResponse = _reflection.GeneratedProtocolMessageType('GetTranscribeAsyncStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSCRIBEASYNCSTATUSRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.GetTranscribeAsyncStatusResponse)
  })
_sym_db.RegisterMessage(GetTranscribeAsyncStatusResponse)

TranscribeAsyncFileStatus = _reflection.GeneratedProtocolMessageType('TranscribeAsyncFileStatus', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIBEASYNCFILESTATUS,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.TranscribeAsyncFileStatus)
  })
_sym_db.RegisterMessage(TranscribeAsyncFileStatus)

GetTranscribeAsyncResultRequest = _reflection.GeneratedProtocolMessageType('GetTranscribeAsyncResultRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSCRIBEASYNCRESULTREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.GetTranscribeAsyncResultRequest)
  })
_sym_db.RegisterMessage(GetTranscribeAsyncResultRequest)

GetTranscribeAsyncResultResponse = _reflection.GeneratedProtocolMessageType('GetTranscribeAsyncResultResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSCRIBEASYNCRESULTRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.GetTranscribeAsyncResultResponse)
  })
_sym_db.RegisterMessage(GetTranscribeAsyncResultResponse)

DeleteTranscribeAsyncFileRequest = _reflection.GeneratedProtocolMessageType('DeleteTranscribeAsyncFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETRANSCRIBEASYNCFILEREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.DeleteTranscribeAsyncFileRequest)
  })
_sym_db.RegisterMessage(DeleteTranscribeAsyncFileRequest)

DeleteTranscribeAsyncFileResponse = _reflection.GeneratedProtocolMessageType('DeleteTranscribeAsyncFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETETRANSCRIBEASYNCFILERESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.DeleteTranscribeAsyncFileResponse)
  })
_sym_db.RegisterMessage(DeleteTranscribeAsyncFileResponse)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.Result)
  })
_sym_db.RegisterMessage(Result)

Word = _reflection.GeneratedProtocolMessageType('Word', (_message.Message,), {
  'DESCRIPTOR' : _WORD,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.Word)
  })
_sym_db.RegisterMessage(Word)

ResultSpeaker = _reflection.GeneratedProtocolMessageType('ResultSpeaker', (_message.Message,), {
  'DESCRIPTOR' : _RESULTSPEAKER,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.ResultSpeaker)
  })
_sym_db.RegisterMessage(ResultSpeaker)

SpeechContext = _reflection.GeneratedProtocolMessageType('SpeechContext', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHCONTEXT,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.SpeechContext)
  })
_sym_db.RegisterMessage(SpeechContext)

SpeechContextEntry = _reflection.GeneratedProtocolMessageType('SpeechContextEntry', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHCONTEXTENTRY,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.SpeechContextEntry)
  })
_sym_db.RegisterMessage(SpeechContextEntry)

CreateSpeechContextRequest = _reflection.GeneratedProtocolMessageType('CreateSpeechContextRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESPEECHCONTEXTREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.CreateSpeechContextRequest)
  })
_sym_db.RegisterMessage(CreateSpeechContextRequest)

CreateSpeechContextResponse = _reflection.GeneratedProtocolMessageType('CreateSpeechContextResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESPEECHCONTEXTRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.CreateSpeechContextResponse)
  })
_sym_db.RegisterMessage(CreateSpeechContextResponse)

DeleteSpeechContextRequest = _reflection.GeneratedProtocolMessageType('DeleteSpeechContextRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESPEECHCONTEXTREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.DeleteSpeechContextRequest)
  })
_sym_db.RegisterMessage(DeleteSpeechContextRequest)

DeleteSpeechContextResponse = _reflection.GeneratedProtocolMessageType('DeleteSpeechContextResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETESPEECHCONTEXTRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.DeleteSpeechContextResponse)
  })
_sym_db.RegisterMessage(DeleteSpeechContextResponse)

ListSpeechContextNamesRequest = _reflection.GeneratedProtocolMessageType('ListSpeechContextNamesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSPEECHCONTEXTNAMESREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.ListSpeechContextNamesRequest)
  })
_sym_db.RegisterMessage(ListSpeechContextNamesRequest)

ListSpeechContextNamesResponse = _reflection.GeneratedProtocolMessageType('ListSpeechContextNamesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSPEECHCONTEXTNAMESRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.ListSpeechContextNamesResponse)
  })
_sym_db.RegisterMessage(ListSpeechContextNamesResponse)

GetSpeechContextRequest = _reflection.GeneratedProtocolMessageType('GetSpeechContextRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSPEECHCONTEXTREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.GetSpeechContextRequest)
  })
_sym_db.RegisterMessage(GetSpeechContextRequest)

GetSpeechContextResponse = _reflection.GeneratedProtocolMessageType('GetSpeechContextResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSPEECHCONTEXTRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.GetSpeechContextResponse)
  })
_sym_db.RegisterMessage(GetSpeechContextResponse)

UpdateSpeechContextRequest = _reflection.GeneratedProtocolMessageType('UpdateSpeechContextRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESPEECHCONTEXTREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.UpdateSpeechContextRequest)
  })
_sym_db.RegisterMessage(UpdateSpeechContextRequest)

UpdateSpeechContextResponse = _reflection.GeneratedProtocolMessageType('UpdateSpeechContextResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESPEECHCONTEXTRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.UpdateSpeechContextResponse)
  })
_sym_db.RegisterMessage(UpdateSpeechContextResponse)

AddSpeakerRequest = _reflection.GeneratedProtocolMessageType('AddSpeakerRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDSPEAKERREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.AddSpeakerRequest)
  })
_sym_db.RegisterMessage(AddSpeakerRequest)

AddSpeakerResponse = _reflection.GeneratedProtocolMessageType('AddSpeakerResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDSPEAKERRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.AddSpeakerResponse)
  })
_sym_db.RegisterMessage(AddSpeakerResponse)

GetSpeakerRequest = _reflection.GeneratedProtocolMessageType('GetSpeakerRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSPEAKERREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.GetSpeakerRequest)
  })
_sym_db.RegisterMessage(GetSpeakerRequest)

GetSpeakerResponse = _reflection.GeneratedProtocolMessageType('GetSpeakerResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSPEAKERRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.GetSpeakerResponse)
  })
_sym_db.RegisterMessage(GetSpeakerResponse)

GetSpeakerResponseAudio = _reflection.GeneratedProtocolMessageType('GetSpeakerResponseAudio', (_message.Message,), {
  'DESCRIPTOR' : _GETSPEAKERRESPONSEAUDIO,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.GetSpeakerResponseAudio)
  })
_sym_db.RegisterMessage(GetSpeakerResponseAudio)

RemoveSpeakerRequest = _reflection.GeneratedProtocolMessageType('RemoveSpeakerRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVESPEAKERREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.RemoveSpeakerRequest)
  })
_sym_db.RegisterMessage(RemoveSpeakerRequest)

RemoveSpeakerResponse = _reflection.GeneratedProtocolMessageType('RemoveSpeakerResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVESPEAKERRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.RemoveSpeakerResponse)
  })
_sym_db.RegisterMessage(RemoveSpeakerResponse)

ListSpeakersRequest = _reflection.GeneratedProtocolMessageType('ListSpeakersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSPEAKERSREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.ListSpeakersRequest)
  })
_sym_db.RegisterMessage(ListSpeakersRequest)

ListSpeakersResponse = _reflection.GeneratedProtocolMessageType('ListSpeakersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSPEAKERSRESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.ListSpeakersResponse)
  })
_sym_db.RegisterMessage(ListSpeakersResponse)

ListSpeakersResponseSpeaker = _reflection.GeneratedProtocolMessageType('ListSpeakersResponseSpeaker', (_message.Message,), {
  'DESCRIPTOR' : _LISTSPEAKERSRESPONSESPEAKER,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.ListSpeakersResponseSpeaker)
  })
_sym_db.RegisterMessage(ListSpeakersResponseSpeaker)

AddSpeakerAudioRequest = _reflection.GeneratedProtocolMessageType('AddSpeakerAudioRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDSPEAKERAUDIOREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.AddSpeakerAudioRequest)
  })
_sym_db.RegisterMessage(AddSpeakerAudioRequest)

AddSpeakerAudioResponse = _reflection.GeneratedProtocolMessageType('AddSpeakerAudioResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDSPEAKERAUDIORESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.AddSpeakerAudioResponse)
  })
_sym_db.RegisterMessage(AddSpeakerAudioResponse)

GetSpeakerAudioRequest = _reflection.GeneratedProtocolMessageType('GetSpeakerAudioRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSPEAKERAUDIOREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.GetSpeakerAudioRequest)
  })
_sym_db.RegisterMessage(GetSpeakerAudioRequest)

GetSpeakerAudioResponse = _reflection.GeneratedProtocolMessageType('GetSpeakerAudioResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSPEAKERAUDIORESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.GetSpeakerAudioResponse)
  })
_sym_db.RegisterMessage(GetSpeakerAudioResponse)

RemoveSpeakerAudioRequest = _reflection.GeneratedProtocolMessageType('RemoveSpeakerAudioRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVESPEAKERAUDIOREQUEST,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.RemoveSpeakerAudioRequest)
  })
_sym_db.RegisterMessage(RemoveSpeakerAudioRequest)

RemoveSpeakerAudioResponse = _reflection.GeneratedProtocolMessageType('RemoveSpeakerAudioResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVESPEAKERAUDIORESPONSE,
  '__module__' : 'soniox.speech_service_pb2'
  # @@protoc_insertion_point(class_scope:soniox.speech_service.RemoveSpeakerAudioResponse)
  })
_sym_db.RegisterMessage(RemoveSpeakerAudioResponse)

_SPEECHSERVICE = DESCRIPTOR.services_by_name['SpeechService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TRANSCRIBEREQUEST._serialized_start=87
  _TRANSCRIBEREQUEST._serialized_end=195
  _TRANSCRIBECONFIG._serialized_start=198
  _TRANSCRIBECONFIG._serialized_end=671
  _TRANSCRIBERESPONSE._serialized_start=673
  _TRANSCRIBERESPONSE._serialized_end=740
  _TRANSCRIBESTREAMREQUEST._serialized_start=742
  _TRANSCRIBESTREAMREQUEST._serialized_end=862
  _TRANSCRIBESTREAMCONFIG._serialized_start=865
  _TRANSCRIBESTREAMCONFIG._serialized_end=1370
  _TRANSCRIBESTREAMRESPONSE._serialized_start=1372
  _TRANSCRIBESTREAMRESPONSE._serialized_end=1445
  _TRANSCRIBEMEETINGREQUEST._serialized_start=1448
  _TRANSCRIBEMEETINGREQUEST._serialized_end=1656
  _TRANSCRIBEMEETINGCONFIG._serialized_start=1659
  _TRANSCRIBEMEETINGCONFIG._serialized_end=1931
  _TRANSCRIBEMEETINGRESPONSE._serialized_start=1934
  _TRANSCRIBEMEETINGRESPONSE._serialized_end=2109
  _TRANSCRIBEASYNCREQUEST._serialized_start=2111
  _TRANSCRIBEASYNCREQUEST._serialized_end=2191
  _TRANSCRIBEASYNCRESPONSE._serialized_start=2193
  _TRANSCRIBEASYNCRESPONSE._serialized_end=2235
  _GETTRANSCRIBEASYNCSTATUSREQUEST._serialized_start=2237
  _GETTRANSCRIBEASYNCSTATUSREQUEST._serialized_end=2304
  _GETTRANSCRIBEASYNCSTATUSRESPONSE._serialized_start=2306
  _GETTRANSCRIBEASYNCSTATUSRESPONSE._serialized_end=2405
  _TRANSCRIBEASYNCFILESTATUS._serialized_start=2408
  _TRANSCRIBEASYNCFILESTATUS._serialized_end=2542
  _GETTRANSCRIBEASYNCRESULTREQUEST._serialized_start=2544
  _GETTRANSCRIBEASYNCRESULTREQUEST._serialized_end=2611
  _GETTRANSCRIBEASYNCRESULTRESPONSE._serialized_start=2613
  _GETTRANSCRIBEASYNCRESULTRESPONSE._serialized_end=2694
  _DELETETRANSCRIBEASYNCFILEREQUEST._serialized_start=2696
  _DELETETRANSCRIBEASYNCFILEREQUEST._serialized_end=2764
  _DELETETRANSCRIBEASYNCFILERESPONSE._serialized_start=2766
  _DELETETRANSCRIBEASYNCFILERESPONSE._serialized_end=2801
  _RESULT._serialized_start=2804
  _RESULT._serialized_end=2968
  _WORD._serialized_start=2971
  _WORD._serialized_end=3104
  _RESULTSPEAKER._serialized_start=3106
  _RESULTSPEAKER._serialized_end=3152
  _SPEECHCONTEXT._serialized_start=3154
  _SPEECHCONTEXT._serialized_end=3243
  _SPEECHCONTEXTENTRY._serialized_start=3245
  _SPEECHCONTEXTENTRY._serialized_end=3297
  _CREATESPEECHCONTEXTREQUEST._serialized_start=3299
  _CREATESPEECHCONTEXTREQUEST._serialized_end=3406
  _CREATESPEECHCONTEXTRESPONSE._serialized_start=3408
  _CREATESPEECHCONTEXTRESPONSE._serialized_end=3437
  _DELETESPEECHCONTEXTREQUEST._serialized_start=3439
  _DELETESPEECHCONTEXTREQUEST._serialized_end=3498
  _DELETESPEECHCONTEXTRESPONSE._serialized_start=3500
  _DELETESPEECHCONTEXTRESPONSE._serialized_end=3529
  _LISTSPEECHCONTEXTNAMESREQUEST._serialized_start=3531
  _LISTSPEECHCONTEXTNAMESREQUEST._serialized_end=3579
  _LISTSPEECHCONTEXTNAMESRESPONSE._serialized_start=3581
  _LISTSPEECHCONTEXTNAMESRESPONSE._serialized_end=3628
  _GETSPEECHCONTEXTREQUEST._serialized_start=3630
  _GETSPEECHCONTEXTREQUEST._serialized_end=3686
  _GETSPEECHCONTEXTRESPONSE._serialized_start=3688
  _GETSPEECHCONTEXTRESPONSE._serialized_end=3776
  _UPDATESPEECHCONTEXTREQUEST._serialized_start=3778
  _UPDATESPEECHCONTEXTREQUEST._serialized_end=3885
  _UPDATESPEECHCONTEXTRESPONSE._serialized_start=3887
  _UPDATESPEECHCONTEXTRESPONSE._serialized_end=3916
  _ADDSPEAKERREQUEST._serialized_start=3918
  _ADDSPEAKERREQUEST._serialized_end=3968
  _ADDSPEAKERRESPONSE._serialized_start=3970
  _ADDSPEAKERRESPONSE._serialized_end=4049
  _GETSPEAKERREQUEST._serialized_start=4051
  _GETSPEAKERREQUEST._serialized_end=4101
  _GETSPEAKERRESPONSE._serialized_start=4104
  _GETSPEAKERRESPONSE._serialized_end=4247
  _GETSPEAKERRESPONSEAUDIO._serialized_start=4249
  _GETSPEAKERRESPONSEAUDIO._serialized_end=4360
  _REMOVESPEAKERREQUEST._serialized_start=4362
  _REMOVESPEAKERREQUEST._serialized_end=4415
  _REMOVESPEAKERRESPONSE._serialized_start=4417
  _REMOVESPEAKERRESPONSE._serialized_end=4440
  _LISTSPEAKERSREQUEST._serialized_start=4442
  _LISTSPEAKERSREQUEST._serialized_end=4480
  _LISTSPEAKERSRESPONSE._serialized_start=4482
  _LISTSPEAKERSRESPONSE._serialized_end=4574
  _LISTSPEAKERSRESPONSESPEAKER._serialized_start=4576
  _LISTSPEAKERSRESPONSESPEAKER._serialized_end=4684
  _ADDSPEAKERAUDIOREQUEST._serialized_start=4686
  _ADDSPEAKERAUDIOREQUEST._serialized_end=4784
  _ADDSPEAKERAUDIORESPONSE._serialized_start=4787
  _ADDSPEAKERAUDIORESPONSE._serialized_end=4920
  _GETSPEAKERAUDIOREQUEST._serialized_start=4922
  _GETSPEAKERAUDIOREQUEST._serialized_end=5005
  _GETSPEAKERAUDIORESPONSE._serialized_start=5008
  _GETSPEAKERAUDIORESPONSE._serialized_end=5156
  _REMOVESPEAKERAUDIOREQUEST._serialized_start=5158
  _REMOVESPEAKERAUDIOREQUEST._serialized_end=5244
  _REMOVESPEAKERAUDIORESPONSE._serialized_start=5246
  _REMOVESPEAKERAUDIORESPONSE._serialized_end=5274
  _SPEECHSERVICE._serialized_start=5277
  _SPEECHSERVICE._serialized_end=7614
# @@protoc_insertion_point(module_scope)
