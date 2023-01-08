import random
import pyautogui

# Declaring some variables
lower = 1
upper = 100
attempts = 0
chances_left = 10

# Generate a random numbers
target = random.randint(lower, upper)

# Show the first Window
pyautogui.alert("Please Guess the Number between 0 and 100. \nYou haves only 10 chances")

# The wile loop will iterate until the user
# attempts t0 10 guesses

while attempts < 10:
    attempts += 1

    guess = pyautogui.prompt(f"Chances left: {chances_left}\nPlease guess the number!")

# Check if the guess matches with the target number
# Convert the guess variable to an interger variable
if int(guess) == target:
    pyautogui.alert(f"Congrats! You did it in {attempts} attempts.")  
elif int(guess) < target:
    pyautogui.alert(f"Sorry, You have chosen a less")
elif int(guess) > target:
    pyautogui.alert(f"Sorry, You have chosen a hight")

chances_left -= 1

# Chech the number of attempts
if attempts >= 10:
    pyautogui.alert(f"Sorry You Lost.\nThe Number is: {target}.")
