import pandas as pd

df = pd.read_csv("./nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Enter a word:").upper()

nato_word = [nato_dict[letter] for letter in word]

print(nato_word)