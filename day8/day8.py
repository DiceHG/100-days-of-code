import string

alphabet = string.ascii_lowercase

def caesar(original_text, shift, mode):
    if mode == 'decode':
        shift = -shift
    
    output_text = ''
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
            continue
        shifted_position = alphabet.index(letter) + shift
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    
    return output_text

while True:
    mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(f'Here is the {mode}d result: {caesar(text, shift, mode)}\n')

    if input("Type 'yes' to continue, type 'no' to stop:\n").lower() == 'no':
        break