#Dice Game!

import random

#Initialize Variables
min = 1
max = 6

#Take input
guess = int(input("Guess a number of a 6-sided die: "))

#Simulate die rolling
print("Rolling a die...")

roll = int(random.randint(min,max))

print("You rolled a: %s" %roll)

#Display appropriate result
if guess == roll:
    print("You guessed correctly!")
else:
    print("You guessed incorrectly!")
