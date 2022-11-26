import random
while True:

    choice = ["rock", "paper", "scissors"]
    computer = random.choice(choice)
    player = None
    while player not in choice:
        player = input("rock, paper, scissors? : ")

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie !!!")
    elif player == "rock":
        if computer == "paper":
            print("computer :", computer)
            print("player :", player)
            print("You are looser !!!")
        if computer == "scissors":
            print("computer :", computer)
            print("player :", player)
            print("You win !!!")
    elif player == "scissors":
        if computer == "rock":
            print("computer :", computer)
            print("player :", player)
            print("You are looser !!!")
        if computer == "paper":
            print("computer :", computer)
            print("player :", player)
            print("You win !!!")
    elif player == "paper":
        if computer == "scissors":
            print("computer :", computer)
            print("player :", player)
            print("You are looser !!!")
        if computer == "rock":
            print("computer :", computer)
            print("player :", player)
            print("You win !!!")

play_again = input("Play again (yes/no) : ").lower()
if play_again != "yes":
    break
print("Bye.")
