from gtts import gTTS
import os
import tempfile

def speak(text, lang):
    lang_codes = {
        "English": "en", "Hindi": "hi", "Telugu": "te", "Tamil": "ta",
        "Kannada": "kn", "Malayalam": "ml", "French": "fr", "German": "de"
    }
    tts = gTTS(text=text, lang=lang_codes.get(lang, "en"))
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        os.system(f"start {fp.name}" if os.name == "nt" else f"mpg123 {fp.name}")

def understand_issue(user_input):
    issues = {
        "battery overheating": "Your battery is overheating. Please park the car safely. I’ll guide you step-by-step.",
        "brake failure": "Brake system failure detected. Reduce speed gradually and stop safely.",
        "charger unplugged": "Charging cable unplugged. Please reconnect the charger.",
        "oil leak": "Oil leakage detected. Please consult a mechanic immediately.",
        "tire pressure low": "Tire pressure is low. Inflate tires to recommended levels."
    }
    for key in issues:
        if key in user_input.lower():
            return issues[key]
    return "Issue not recognized. Please consult a mechanic."
