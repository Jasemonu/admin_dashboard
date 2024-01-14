from translate import Translator

translator = Translator(to_lang='zu')

texts_to_translate = ['The quick brown fox', 'jumps over', 'the lazy dog']

try:
    translations = [translator.translate(text) for text in texts_to_translate]
    print("API Response:", translations)

    for original, translation in zip(texts_to_translate, translations):
        print(f"{original} --> {translation}")

except AttributeError as ae:
    print(f"AttributeError: {ae}")

except Exception as e:
    print(f"An error occurred: {e}")
