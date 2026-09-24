# Dictionary Project

translations = {
    "hello": "హలో",
    "good morning": "శుభోదయం",
    "thank you": "ధన్యవాదాలు",
    "good night": "శుభ రాత్రి",
    "how are you": "మీరు ఎలా ఉన్నారు?"
}

text = input("Enter English text: ")

text = text.lower()

if text in translations:
    print("Telugu:", translations[text])
else:
    print("Translation not available")