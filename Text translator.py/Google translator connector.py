from deep_translator import GoogleTranslator

text = input("Enter text: ")

source = input("Enter source language (example: en): ")
target = input("Enter target language (example: te): ")

translated_text = GoogleTranslator(
    source=source,
    target=target
).translate(text)

print("Translated text:", translated_text)