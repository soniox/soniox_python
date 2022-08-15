from soniox.transcribe_file import transcribe_file_stream
from soniox.speech_service import Client, set_api_key
from soniox.test_data import TEST_AUDIO_SD_FLAC

set_api_key("<YOUR-API-KEY>")


def main():
    with Client() as client:
        result = transcribe_file_stream(
            TEST_AUDIO_SD_FLAC,
            client,
            enable_global_speaker_diarization=True,
            min_num_speakers=1,
            max_num_speakers=6,
        )

    speaker = None
    for word in result.words:
        if word.speaker != speaker:
            if speaker is not None:
                print()
            speaker = word.speaker
            print(f"Speaker {speaker}: ", end="")
        else:
            print(" ", end="")
        print(word.text, end="")
    print()


if __name__ == "__main__":
    main()
