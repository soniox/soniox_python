import subprocess
from shlex import quote as _q


def convert_to_flac_file(input_file: str, output_flac_file: str) -> None:
    cmd = f"ffmpeg -loglevel error -y -i {_q(input_file)} -f flac -c:a flac -ac 1 -ar 16000 -sample_fmt s16 {_q(output_flac_file)}"
    subprocess.run(cmd, shell=True, check=True)
