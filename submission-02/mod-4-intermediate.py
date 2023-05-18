def shift_letter(letter, shift):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if letter == " ":
        return " "
    else:
        letter = letter.upper()
        index = alphabet.index(letter)
        shifted_index = (index + shift) % len(alphabet)
        shifted_letter = alphabet[shifted_index]
        return shifted_letter

def caesar_cipher(message, shift):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    shifted_message = ""
    
    for letter in message:
        if letter == " ":
            shifted_message += " "
        else:
            letter = letter.upper()
            index = alphabet.index(letter)
            shifted_index = (index + shift) % len(alphabet)
            shifted_letter = alphabet[shifted_index]
            shifted_message += shifted_letter
    
    return shifted_message

def shift_by_letter(letter, letter_shift):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    if letter == " ":
        return " "
    else:
        letter = letter.upper()
        letter_shift = letter_shift.upper()
        shift_value = alphabet.index(letter_shift)
        index = alphabet.index(letter)
        shifted_index = (index + shift_value) % len(alphabet)
        shifted_letter = alphabet[shifted_index]
        return shifted_letter

def vigenere_cipher(message, key):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    encrypted_message = ""
    extended_key = ""
    key_length = len(key)
    message_length = len(message)

    if key_length >= message_length:
        extended_key = key[:message_length]
    else:
        repetitions = message_length // key_length
        remainder = message_length % key_length
        extended_key = key * repetitions + key[:remainder]

    for i in range(len(message)):
        char = message[i]
        if char == " ":
            encrypted_message += " "
        else:
            char = char.upper()
            key_letter = extended_key[i]
            key_letter = key_letter.upper()
            shift_value = alphabet.index(key_letter)
            index = alphabet.index(char)
            shifted_index = (index + shift_value) % len(alphabet)
            shifted_char = alphabet[shifted_index]
            encrypted_message += shifted_char

    return encrypted_message




