import random


def check_number(usr_guess, number, tries_left):
    if usr_guess > number:
        if tries_left - 1 == 0:
            print(f"Too bad you lost. The correct number was {number}.")
        else:
            print("Too high.\nGuess again.")
        return tries_left - 1
    elif usr_guess < number:
        if tries_left - 1 == 0:
            print(f"Too bad you lost. The correct number was {number}.")
        else:
            print("Too low.\nGuess again.")
        return tries_left - 1
    else:
        print(f"You got it! The answer was: {number}")
        return 0


print("Welcome to Guess The Number!")
print("I'm thinking of a number between 1 and 100")
game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

the_number = random.randint(1, 100)

if game_mode == "easy":
    num_tries = 10
elif game_mode == "hard":
    num_tries = 5
else:
    print("You have entered an invalid game mode. Goodbye.")
    exit()

while num_tries > 0:
    print(f"You have {num_tries} attempts remaining to guess the number.")
    guess = input("Make a guess: ")
    try:
        guess = int(guess)
        pass
    except ValueError as ve:
        print("You've entered an invalid number")
        num_tries -= 1
        if num_tries == 0:
            print(f"Too bad you lost. The correct number was {the_number}.")
        continue

    num_tries = check_number(guess, the_number, num_tries)