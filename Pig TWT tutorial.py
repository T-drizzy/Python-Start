import random 
import time

#Defing what a roll is. Which is a value between 1 and 6 (the resemblance of a dice).
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

#Checking the amount of players, and making sure that its a digit and between 2-4
while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 or 4 players.")
    else:
        print("Invalid, try again.")

#Creating the max score
max_score = 50

#Creating the individual scores for the amount of players in the first while loop
player_scores = [0 for _ in range(players)]

#Simulating the game, as long as the player score is less than the max of 50
while max(player_scores) < max_score:
    #Here our for loop begins. So for each player (player_idx),the game will print whos turn it is.
    #Then tell you what the score of that player is. The for loop will do this until 'while max(player_scores) < max_score:' is broken.
    for player_idx in range(players):
        print("\n Player number ",player_idx + 1, "turn has just started!")
        print("Your total score is: ", player_scores[player_idx], "\n")
        
        current_score = 0
        #This while loop will run until a player inputs something else than y or when the player rolls a 1
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()

            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break

            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is: ", current_score)
    
        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)