LANGUAGE_CODES = {
    "en": "English",
    "hi": "Hindi",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh": "Chinese",
    "ru": "Russian",
    "ar": "Arabic",
    "pt": "Portuguese",
    "nl": "Dutch",
    "tr": "Turkish",
    "pl": "Polish",
    "sv": "Swedish",
    "uk": "Ukrainian",
    "ta": "Tamil",
    "te": "Telugu",
    "bn": "Bengali",
    "mr": "Marathi",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "ur": "Urdu"
}


def get_language_name(code):
    return LANGUAGE_CODES.get(code, code)