import random
from wordsForhangman import words

def get_valid_word(words):
    valid_word=random.choice(words)
    while '-' in valid_word or ' ' in valid_word:
        valid_word = random.choice(words)
    return valid_word.upper()

print (get_valid_word(words))