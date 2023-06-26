import random
#Introduction
print("")
print("---------This is a Dice Roll Simulator---------")
print("")
#Dice Roll funtion
def dice_roll(dice, sides):
    roll = []
    
    for i in range(0,dice):
        face = random.randint (1, sides)
        roll.append(face)
    
    return roll

#Dice variables
dice = int(input("Number of die you want to roll with: "))
if (dice < 1):
    print("You must use at least one dice")
    quit()

sides = int(input("How many sides on your die?: "))
if (sides < 1):
    print("A dice with no sides, is not a dice... its a cube")
    quit()

roll = dice_roll(dice,sides)

random.randint(1,sides)

print ("You rolled: " + str(roll))

# Statistics
total_rolls = len(roll)
sum_rolls = sum(roll)
average_roll = sum_rolls / total_rolls

print("----- Statistics -----")
print("Total Rolls:", total_rolls)
print("Sum of Rolls:", sum_rolls)
print("Average Roll:", average_roll)