import argparse
import glob
from multiprocessing import Pool
from soniox.speech_service import Client, set_api_key
from soniox.transcribe_file import transcribe_file_stream

set_api_key("<YOUR-API-KEY>")


def process_file(audio_fn: str) -> None:
    with Client() as client:
        # Create output text file.
        output_fn = audio_fn + ".txt"
        with open(output_fn, "w") as output_file:
            # Keep track of total processed audio duration.
            duration_ms = 0
            # Trancribe file.
            for result in transcribe_file_stream(audio_fn, client):
                words = [word.text for word in result.words]
                output_file.write(" ".join(words) + "\n")
                duration_ms = result.final_proc_time_ms
            # Write total processed audio duration.
            output_file.write(f"duration_ms={duration_ms}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Transcribe audio files in parallel.")
    parser.add_argument(
        "--glob_pathname", type=str, help="Audio files to transcribe."
    )
    parser.add_argument("--processes", type=int, default=4)
    args = parser.parse_args()
    assert args.processes >= 1

    # Get audio files to be transcibed.
    audio_files = glob.glob(args.glob_pathname)
    if len(audio_files) == 0:
        raise Exception("No files found.")

    # Transcribe in parallel with specified number of processes.
    with Pool(args.processes) as pool:
        for i, _ in enumerate(pool.imap_unordered(process_file, audio_files)):
            print(f"\rFinished {i+1} files out of {len(audio_files)}", end="")
        print()


if __name__ == "__main__":
    main()
