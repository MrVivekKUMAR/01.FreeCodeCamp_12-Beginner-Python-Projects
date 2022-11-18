import random
def play():
    user = input ("Choice rock [R], paper [P] or Scissors [S] :").lower()
    computerChoice = random.choice(['r','p','s'])
    print (f"Computer choice is {computerChoice}")

    if user==computerChoice:
        return "It is Tie !"

    if is_Win(user,computerChoice):
        return "Congratulations , You won and I lost"

    return "Computer won"

def is_Win(user , computerChoice):
    # r > s ; s > p ; p > r
    if (user=='r' and computerChoice =='s' ) or (user=='s' and computerChoice =='p') or (user=='p' and computerChoice =='r'):
        return True

print (play())