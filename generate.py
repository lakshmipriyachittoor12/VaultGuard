import string
import random

def generate_pass(min_len, numbers=True, special=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special:
        characters += special_chars
    
    pwd = ""
    meets = False
    has_num = False
    has_special = False

    while not meets or len(pwd) < min_len:
        new_char = random.choice(characters)
        pwd += new_char
        if new_char in digits:
            has_num = True
        elif new_char in special_chars:
            has_special = True
        
        meets = True
        if numbers:
            meets = has_num
        if special:
            meets = meets and has_special
    return pwd
