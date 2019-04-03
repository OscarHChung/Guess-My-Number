import random

min = 0
max = 100
attempts = 0
num = random.randint(min, max)
yesno = True

print("Welcome to the Guess My Number Game.  I chose a number between " + str(min) + "-" + str(max))

while yesno:
    guess = int(input("Please guess a number:"))
    if guess >= 0 and guess <= 100:
         if guess == num:
             attempts = attempts + 1
             play = input("You won! It took you " + str(attempts) + " attempts. Would you like to play again?")
             if play == "no":
                 yesno = False
             else:
                 num = random.randint(min, max)
                 yesno = False
                 yesno = True
         elif guess > num:
             print("This number is too big.")
             attempts = attempts + 1
         else:
             print("This number is too small.")
             attempts = attempts + 1
    else:
        print("Give a valid input.")
