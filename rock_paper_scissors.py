# rock_paper_scissors, you play against with computer
import random

# define a function for rules, the rule is 'r > s, s > p, p > r'
def play(player,opponent):
if (player=="r" and opponent =="s") or (player=="s" and opponent=="p") or \
    (player=="p" and opponent == "r"):
    return True
return False

# make a for loop if tie game
while True:

    player_choice = str(input("r for Rock, p for Paper, s for scissors, now make your chocice \
        (r/p/s): "))

    # computer choose a random choice
    opponent_choice = random.choice(["r","p","s"])

    # situation for tie game
    if player_choice == opponent_choice:
        print("tie game")
        continue
    else:
        # call the rule function and output
        if play(player_choice,opponent_choice)==True:
            print(f"You win, computer \'choice is {opponent_choice}")
        print(f"You lost, computer \'choice is {opponent_choice}")
        break
