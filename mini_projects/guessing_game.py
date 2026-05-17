import random
lowest = 1
highest  =100
answer = random.randint(lowest,highest)
guesses = 0
is_running = True
print("---Welcome to the number guessing game---")
print(f"Select the number between {lowest} - {highest}")

while is_running:
    guess = input("Enter your guess : ")

    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        if guess<lowest or guess>highest:
            print("The number is out of range")
            print(f"Select the number between {lowest} - {highest}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high, Try again!")
        else:
            print()
            print("----------------------------------")
            print(f"The correct answer was {answer}")
            print(f"Number of guesses : {guesses}")
            is_running =False
    else:
        print("Ivalid guess")
        print(f"Select the number between {lowest} - {highest}")