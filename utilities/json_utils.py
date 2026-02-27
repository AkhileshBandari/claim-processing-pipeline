import json
import re

def safe_json_parse(text):
    try:
        return json.loads(text)
    except:
        cleaned = re.sub(r"```json|```", "", text).strip()
        return json.loads(cleaned)

def clean_number(value):
    if isinstance(value, str):
        value = value.replace("$", "").replace(",", "").strip()
    return float(value)