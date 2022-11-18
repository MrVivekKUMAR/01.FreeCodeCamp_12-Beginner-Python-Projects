# Number guessing game


import random as rn

def random_number(x):
    random_no=rn.randint(1,x)
    guess_no = 0
    while (guess_no != random_no):
        guess_no = int(input(f"Enter a guess number between 1 and {x} :"))
        if (guess_no > random_no):
            print ("Sorry your guess is higher then secrete Number")
        elif (guess_no < random_no):
            print ("Sorry your guess is lower then secrete Number")
    print (f"Congratulation ! You guessed correct number {random_no}")

random_number(100)