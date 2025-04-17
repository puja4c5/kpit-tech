import json
import os

def load_responses(language_code='en'):
    responses_dir = os.path.join('data', 'multilingual_responses')
    file_path = os.path.join(responses_dir, f"{language_code}.json")
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {"unplugged_device": "Sorry, I cannot find responses in your selected language."}

def get_instruction(issue="unplugged_device", language_code="en"):
    responses = load_responses(language_code)
    return responses.get(issue, "No response available for this issue.")
