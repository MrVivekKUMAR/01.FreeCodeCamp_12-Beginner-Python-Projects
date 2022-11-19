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
    lives = 6

    while (len(word_letter) > 0) and lives > 0:
        print ('you have ',lives , 'left. Used letters are : ', ' '.join(used_letter))
        user_input = input("Guess a Letter :").upper()

        if user_input in alphabet - used_letter:
            used_letter.add(user_input)
            if user_input in word_letter:
                    word_letter.remove(user_input)
            else:
                lives-=lives # Take Away the life if user is wrong
                print (f"letter {user_input} is not in list ")
        elif user_input in used_letter:
            print ("you have already Try this letter, Please try another letter")
        else:
            print ("Please try a valid Charector")

        current_word = [letter if letter in used_letter else '-' for letter in word]

        if lives==0:
            print ("you are died")
        else:
            print ('Current word is : ', ' '.join(current_word))

hang_man()