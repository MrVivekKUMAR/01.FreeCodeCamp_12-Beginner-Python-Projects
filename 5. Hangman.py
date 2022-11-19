import random
import string

from wordsForhangman import words

def get_valid_word(words):
    valid_word=random.choice(words)
    while '-' in valid_word or ' ' in valid_word:
        valid_word = random.choice(words)
    return valid_word.upper()


def hang_man():
    word= (get_valid_word(words))
    word_letter=set(word) # save the word in an list for e.g for a word= BUMP the word_letter is {'P', 'U', 'M', 'B'}
    alphabet = set(string.ascii_uppercase)
    used_letter=set()

def


