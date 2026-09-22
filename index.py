# Dictionary - Basic Text Translator
def translate_text(text, source_language, target_language):
    print("Translation started...")
    print(f"From: {source_language}")
    print(f"To: {target_language}")
    print(f"Text: {text}")

    # Basic example
    translations = {
        "hello": "hi",
        "thank you": "dhanyavaad",
        "good morning": "suprabhaat"
    }

    result = translations.get(text.lower(), "Translation not available")

    return result

# Get input from the user
text = input("Enter text: ")
source_language = input("Enter source language: ")
target_language = input("Enter target language: ")

# Translate
result = translate_text(text, source_language, target_language)

print("Translated text:", result)