from translate import Translator


def translate_to_hebrew(word):
    translator = Translator(to_lang='he')
    translation = translator.translate(word)
    return translation


word_to_translate = "smiling to myself"
hebrew_translation = translate_to_hebrew(word_to_translate)
print(hebrew_translation)
