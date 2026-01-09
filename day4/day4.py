from random import randint

# Rock, Paper, Scissors
ascii_images = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
print(ascii_images[user_choice])

computer_choice = randint(0, 2)
print('Computer chose: \n', ascii_images[computer_choice])

if computer_choice == user_choice:
    print('It\'s a draw')
elif computer_choice - user_choice == -1 or computer_choice - user_choice == 2:
    print('You win!')
elif computer_choice - user_choice == 1 or computer_choice - user_choice == -2:
    print('You lose...')