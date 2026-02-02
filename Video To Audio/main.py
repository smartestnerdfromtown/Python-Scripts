import subprocess

subprocess.run([
    "ffmpeg",
    "-i", "videos/video.mp4",
    "-vn",
    "-ac", "1",
    "-ar", "16000",
    "video.wav"
], check=True)


