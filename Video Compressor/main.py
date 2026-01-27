from pathlib import Path
import subprocess

VIDEO_DIR = Path("videos")
CRF_VALUE = 28
PRESET = "slow"

def size_mb(path: Path) -> str:
    size = path.stat().st_size / 1024 / 1024
    return f"{size:.2f} MB"

def compress(input_path: Path):
    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_path}")

    VIDEO_DIR.mkdir(exist_ok=True)

    output_path = input_path.with_name(
        f"{input_path.stem}_compressed{input_path.suffix}"
    )

    print(f"Compressing: {input_path.name}")
    print(f"Output: {output_path}")

    subprocess.run([
        "ffmpeg",
        "-y",                     # overwrite without prompt
        "-i", str(input_path),
        "-c:v", "libx264",
        "-crf", str(CRF_VALUE),   # Classic is 23, but I needed stronger compression.
        "-preset", PRESET,
        "-c:a", "copy",
        str(output_path)
    ], check=True)

    return output_path

def main() -> None:
    input_file = VIDEO_DIR / "Шифрование.mp4"

    print(f"Working directory: {Path.cwd()}")
    size_before = size_mb(input_file)
    
    output_file = compress(input_file)
    size_after = size_mb(input_file)

    print(f"Before: {size_before}")
    print(f"After: {size_after}")


if __name__ == "__main__":
    main()