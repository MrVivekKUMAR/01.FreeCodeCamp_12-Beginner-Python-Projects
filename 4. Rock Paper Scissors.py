import random
def play():
    user = input ("Choice rock [R], paper [P] or Scissors [S] :").lower()
    computer_choice = random.choice(['r','p','s'])
    print (f"Computer choice is {computer_choice}")

    if user==computer_choice:
        return "It is Tie !"

    if is_Win(user,computer_choice):
        return "Congratulations , You won and I lost"

    return "Computer won"

def is_win(user, computer_choice):
    # The rule of the game is , so when it follow this rule it return True r > s ; s > p ; p > r
    if (user =='r' and computer_choice == 's') or (user == 's' and computer_choice == 'p') or (user == 'p' and computer_choice == 'r'):
        return True

print (play())