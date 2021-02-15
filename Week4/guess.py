import random

numberToGuess = random.randint(1,100)
userGuess = input("Please guess a number:")

while int(userGuess) != numberToGuess:
    print("wrong")
    if int(userGuess) > numberToGuess:
        print("Too high")
    else:
        print("Too low")
    userGuess = input("Please guess again:")

else: 
    print("Good job, {} was the correct number".format(userGuess))