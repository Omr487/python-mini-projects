import random
options = ("rock","paper","scissor")

runnning = True

while runnning:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock,paper,scissor): ")
    print(f"Player : {player}")
    print(f"computer : {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer =="scissor":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you win")
    elif player == "scissor" and computer =="paper":
        print("you win")
    else :
        print("you lose !")
     

    if not input("play again (y/n):").lower() =="y":
        runnning = False

print("thanks for playing")