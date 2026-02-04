with open("./Input/Names/invited_names.txt", "r") as names_file, open("/Users/dudug/Desktop/100days/day24/Input/Letters/starting_letter.txt") as letter_file:
    names = names_file.readlines()
    letter_template = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        letter = letter_template.replace("[name]", stripped_name)

        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", "w") as output_file:
            output_file.write(letter)
        