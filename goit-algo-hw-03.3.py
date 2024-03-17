import re

def normalize_phone(phone_number):
    digits = re.sub(r'\D', '', phone_number)
    if digits.startswith("380"):
        return "+" + digits
    elif digits.startswith("0"):
        return "+38" + digits
    else:
        return "+380" + digits
    

print(normalize_phone("sldgpjglakdfgnsjdg95vsoj117fko90jfswop67"))
