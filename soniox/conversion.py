import subprocess
from typing import Iterable


def convert_to_flac_file(input_file: str, output_flac_file: str) -> None:
    cmd = f"ffmpeg -loglevel error -y -i {input_file} -f flac -c:a flac -ac 1 -ar 16000 -sample_fmt s16 {output_flac_file}"
    subprocess.run(cmd, shell=True, check=True)
