from random import choice
from hangman_art import stages, logo
from hangman_words_list import words_list

print(logo)

choosen_word = choice(words_list)
correct_letters = set(choosen_word)

print('Secret Word: ')
print(choosen_word)

guesses = set()
lives = 6

while lives > 0:
    guess = input('Guess a letter: ').lower()
    
    if len(guess) > 1:
        print(f'Invalid guess')
        continue
    if guess in guesses:
        print(f'You already guessed \'{guess}\'')
    elif guess not in correct_letters:
        lives -= 1
        print(f'The word doesn\'t have any \'{guess}\', you have {lives} lives remaining')
    guesses.add(guess)

    display = ''

    for letter in choosen_word:
        if letter in guesses:
            display += letter
        else:
            display += '_'

    print(display)

    if '_' not in display:
        break

    print(stages[lives])

if lives > 0:
    print('You Win!')
else:
    print(f'The word was {choosen_word}. You Lose')