from random import randint

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

random_number = randint(1, 100)

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > random_number:
        print("Too high.")
    elif guess < random_number:
        print("Too low.")
    else:
        break

    attempts -= 1
    print("Guess again")

if attempts > 0:
    print(f"You got it! The number was {random_number}")
else:
    print(f"You've run out of guesses, you lose. The number was {random_number}")