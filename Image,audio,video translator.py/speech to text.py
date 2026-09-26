import speech_recognition as sr

recognizer = sr.Recognizer()

# Load audio file
with sr.AudioFile("audio.wav") as source:
    audio = recognizer.record(source)

# Convert speech to text
try:
    text = recognizer.recognize_google(audio)
    print("Extracted Text:")
    print(text)

except sr.UnknownValueError:
    print("Could not understand the audio.")

except sr.RequestError as e:
    print("Speech recognition service error:", e)