from data import data
from art import logo, versus_ascii
from random import sample, choice

def game():
    score = 0
    options = sample(data, k=2)

    while True:
        print(logo)
        print(f'Score: {score}')
        print(f'Option A: {options[0]["name"]}, a {options[0]["description"]}, from {options[0]["country"]}')
        print(versus_ascii)
        print(f'Option B: {options[1]["name"]}, a {options[1]["description"]}, from {options[1]["country"]}')
        guess = input("Who has more followers? Type 'a' or 'b': ")

        if guess == 'a':
            if options[0]["follower_count"] < options[1]["follower_count"]:
                break
        else:
            if options[0]["follower_count"] > options[1]["follower_count"]:
                break

        score += 1
        options = [options[1], choice(data)]
    
    print(f"Sorry, that's wrong. Final score: {score}")

if __name__ == '__main__':
    game()