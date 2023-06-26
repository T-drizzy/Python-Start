import random

#Guess variables
guess_range = 50
guesses_allowed = 5
answer = random.randint(1, guess_range)

#Introduction
print("")
print("Welcome to the number geussing game")
print("")

#Player geuss
userInput = input("Guess a number between 1 and "+str(guess_range)+": ")
guess = int(userInput)

#Checking if player is right or wrong
for i in range(guesses_allowed):
    if guess == answer:
        print("YES THATS MY TEMPO!")
        break
    elif guess < answer:
        print("You're dragging. It's not quite my tempo")
    else:
        print("Not quite my tempo. You're rushing")
    if (i == guesses_allowed -1):
        print("I didn't know they allowed retards in here!")
        break
    
    userInput = input("Try it again!: ")
    guess = int(userInput)



