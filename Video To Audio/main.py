import subprocess
from pathlib import Path

BASE_DIR = Path("output_audio")

def video_to_audio(filepath: Path):
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    filename = filepath.stem
    file_extension = filepath.suffix

    output_path = BASE_DIR / f"{filename}.wav"

    subprocess.run([
        "ffmpeg",
        "-i", filepath,
        "-vn",
        "-ac", "1",
        "-ar", "16000",
        output_path
    ], check=True)

video_to_audio(filepath=Path("input_video/video.mp4"))

