import os
from numpy import round
import subprocess

print(os.chdir("Python-Scripts/Video Compressor"))

def size_mb(path):
    return f"{round(os.path.getsize(path) / 1024 / 1024, 2)} MB"


if __name__ == "__main__":
    filepath = "videos/Шифрование.mp4"
    size_before = size_mb(path=filepath)
    print(size_before)