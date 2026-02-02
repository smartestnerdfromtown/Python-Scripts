import subprocess
from pathlib import Path

BASE_DIR = Path("output_audio")
SUPPORTED_AUDIO_FORMATS = {
    "wav", 
    "mp3", 
    "aac", 
    "flac", 
    "ogg", 
    "opus", 
    "m4a"
}

def video_to_audio(
        filepath: str,
        output_format: str = "wav"
    ):
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    output_format = output_format.lower().lstrip(".")

    if output_format not in SUPPORTED_AUDIO_FORMATS:
        raise ValueError(
            f"Unsupported audio format: {output_format}. "
            f"Supported formats: {', '.join(SUPPORTED_AUDIO_FORMATS)}"
        )

    BASE_DIR.mkdir(parents=True, exist_ok=True)

    filename = filepath.stem
    file_extension = filepath.suffix
    output_path = BASE_DIR / f"{filename}.{output_format}"

    subprocess.run([
        "ffmpeg",
        "-i", str(filepath),
        "-vn",
        "-ac", "1",
        "-ar", "16000",
        str(output_path)
    ], check=True)

video_to_audio(
    filepath=("input_video/video.mp4"),
    output_format="MP4")

