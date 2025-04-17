from googletrans import Translator

def translate(text, lang):
    lang_map = {
        "English": "en", "Hindi": "hi", "Telugu": "te", "Tamil": "ta",
        "Kannada": "kn", "Malayalam": "ml", "French": "fr", "German": "de"
    }
    translator = Translator()
    return translator.translate(text, dest=lang_map.get(lang, "en")).text
