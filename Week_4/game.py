import random

# get a positive number from the user
while True:
    try:
        number = int(input("Level: " ))
        if number > 0:
            break
    except ValueError:
        pass

# generate a random number between 1 and the user's number
target = random.randint(1, number)

# don't stop until the user guesses the number
while True:
    try:
        guess = int(input("Guess: "))
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass