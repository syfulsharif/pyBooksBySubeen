import random

number = random.randint(1, 1000)
attempts = 0

while True:
    input_number = int(input("Guess a number between 1 and 1000\n"))
    attempts += 1

    if input_number == number:
        print("Your guess is correct")
        break
    if input_number > number:
        print("Incorrect! Please try a smaller number")
    else:
        print("Incorrect!, Please try to guess a larger number")

print(f"You tried {attempts} to guess the correct number")
