import whisper

model = whisper.load_model("tiny")

result = model.transcribe(
    audio="audio.mp3",
    language="en"
)

print(result["text"])
