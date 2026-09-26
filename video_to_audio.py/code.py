import subprocess

input_video = "input.mp4"
output_audio = "audio.wav"

subprocess.run([
    "ffmpeg",
    "-i", input_video,
    "-vn",
    "-acodec", "pcm_s16le",
    output_audio
])

print("Audio extracted successfully!")