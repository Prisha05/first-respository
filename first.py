import random
enter_game=input("Enter player name=")
print(enter_game)
user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print((enter_game),f" chose {user_action}, computer chose {computer_action}.")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print(("Rock smashes scissors!") ,(enter_game),("You win!"))
    else:
        print(("Paper covers rock!"),(enter_game),("lose"))
elif user_action == "paper":
    if computer_action == "rock":
        print(("Paper covers rock!") ,(enter_game),("You win!"))
    else:
        print(("paper covers rock!"),(enter_game),("lose"))

elif user_action == "scissors":
    if computer_action == "paper":
        print(("Scissors cuts paper!") ,(enter_game),("You win!"))
    else:
        print(("Rock smashes scissors!"),(enter_game),("lose"))
