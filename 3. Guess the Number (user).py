import random
def guessNumber(x):
    low = 1
    high = x
    feedback =0
    c=1
   # print (f"C is {c} and feedback is {feedback}")
    while feedback !=c:
       # print ("inside loop")
        guess = random.randint(low,high)
        print (f'The number is {guess}')
        feedback=input(f"Is number guesses is higher (H) , Lower (L) or Correct (C)?").lower()
        if feedback=='h':
            high=guess-1
         #   print (f"the value of high is changed to {high} and value of low is {low}")
        elif feedback=='l':
           low=guess+1
         #  print (f"the value of high is {high} and value of low is changed to {low}")
        else:
            c=feedback
            print (f"Thank you for your feedback, guessed number is {guess}")


guessNumber(10)