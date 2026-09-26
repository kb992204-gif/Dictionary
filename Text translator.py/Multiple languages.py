from deep_translator import GoogleTranslator
from deep_translator.exceptions import TooManyRequests

languages = {
    "1": ("English", "en"),
    "2": ("Hindi", "hi"),
    "3": ("Telugu", "te"),
    "4": ("Tamil", "ta"),
    "5": ("Kannada", "kn"),
    "6": ("Malayalam", "ml"),
    "7": ("Bengali", "bn"),
    "8": ("Gujarati", "gu"),
    "9": ("Marathi", "mr"),
    "10": ("Punjabi", "pa"),
    "11": ("Odia", "or"),
    "12": ("Assamese", "as"),
    "13": ("Urdu", "ur"),
    "14": ("Nepali", "ne"),
    "15": ("Sanskrit", "sa")
}

print("===== Indian Language Translator =====")

for number, (name, code) in languages.items():
    print(f"{number}. {name}")

source_choice = input("\nEnter source language number: ")
target_choice = input("Enter target language number: ")

if source_choice not in languages or target_choice not in languages:
    print("Invalid language selection.")
    exit()

source_name, source_code = languages[source_choice]
target_name, target_code = languages[target_choice]

text = input(f"\nEnter text in {source_name}: ")

try:
    translated_text = GoogleTranslator(
        source=source_code,
        target=target_code
    ).translate(text)

    print("\n===== Translation Result =====")
    print("Source language:", source_name)
    print("Target language:", target_name)
    print("Original text:", text)
    print("Translated text:", translated_text)

except TooManyRequests:
    print("\nGoogle Translate request limit reached.")
    print("Please wait a few minutes and try again.")

except Exception as e:
    print("\nTranslation failed.")
    print("Error:", e)