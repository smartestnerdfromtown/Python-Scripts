import os
from numpy import round
import pathlib
import subprocess

print(os.getcwd())

def size_mb(path):
    return f"{round(os.path.getsize(path) / 1024 / 1024, 2)} MB"

def compress(path):
    basename = pathlib.Path(path).stem
    extension = pathlib.Path(path).suffix
    output_filepath = f"videos/{basename}_compressed{extension}"
    
    print(basename, extension, output_filepath)

    subprocess.run([
        "ffmpeg",
        "-i", path,
        "-c:v", "libx264",
        "-crf", "28", # Classic is 23, but I needed stronger compression.
        "-preset", "slow",
        "-c:a", "copy",
        output_filepath
    ], check=True)

    return output_filepath

def main():
    pass

if __name__ == "__main__":
    main()
    
    filepath = "videos/Шифрование.mp4"
    size_before = size_mb(path=filepath)
    output_filepath = compress(path=filepath)
    size_after = size_mb(path=output_filepath)
    print(size_before)
    print(size_after)