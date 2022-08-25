import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
win_messages = ["Nice, you won!", "Congrats, you won!", "Good, you won"]
lose_messages = ["You lost this round", "Unlucky you lost this round", "Computer won this one, try again"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input =="q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)

    computer_pick = options[random_number]

    win_mgs = win_messages[random_number]

    lose_msg = lose_messages[random_number]

    if user_input == "rock" and computer_pick == "scissors":
        print(win_mgs)
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print(win_mgs)
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print(win_mgs)
        user_wins += 1
    else:
        print(lose_msg)
        computer_wins += 1

if user_wins == computer_wins:
    print("It is a tie!", user_wins, "to", computer_wins)
elif user_wins > computer_wins:
    print("You beat the computer by", user_wins, "to", computer_wins)
else:
    print("You lost to the computer", user_wins, "to", computer_wins, ". Better luck next time")