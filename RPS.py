from random import randint

word = ["rock", "paper", "scissors"]

computer = word[randint(0,2)]

player = False

while player == False:
    player = input("\x1b[38;2;13;199;206m rock, paper, scissors ? \n\x1b[m")
    if player == computer:
        print("\x1b[38;2;22;202;6m Tie !!\x1b[m")
    elif player == "rock":
        if computer == "paper":
            print("\x1b[38;2;245;75;75m You lose !!\x1b[m", computer, "covers", player)
        else:
            print("\x1b[38;2;213;216;36m You win !!\x1b[m", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("\x1b[38;2;245;75;75m  You lose !!\x1b[m", computer, "cut", player)
        else:
            print("\x1b[38;2;213;216;36m You win !!\x1b[m", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("\x1b[38;2;245;75;75m  You lose !!\x1b[m", computer, "smashes", player)
        else:
            print("\x1b[38;2;213;216;36m You win !!\x1b[m", player, "cut", computer)
    else:
        print("That`s not a valid play. Check your spelling")

    player = False
    computer = word[randint(0,2)]
