from soniox.transcribe_live import transcribe_capture
from soniox.capture_device import SimulatedCaptureDevice
from soniox.speech_service import Client, set_api_key
from soniox.test_data import TEST_AUDIO_SD_RAW

set_api_key("<YOUR-API-KEY>")


def main():
    with Client() as client:
        sim_capture = SimulatedCaptureDevice(TEST_AUDIO_SD_RAW)
        for result in transcribe_capture(
            sim_capture, client, enable_streaming_speaker_diarization=True
        ):
            print(" ".join(f"{w.text}/{w.speaker}" for w in result.words))


if __name__ == "__main__":
    main()
