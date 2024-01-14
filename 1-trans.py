from translate import Translator

def translate_text(text, target_language='ko'):
    translator= Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

# Example usage
text_to_translate = 'The quick brown fox jumps over the lazy dog'
translated_text = translate_text(text_to_translate, target_language='ko')

print(f"Original: {text_to_translate}")
print(f"Translated: {translated_text}")

