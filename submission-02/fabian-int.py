def shift_letter(letter, shift): 

    x = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ")
    
    letter_index = x.index(letter)

    if letter_index <= shift:
        value = x[x.index(letter)+shift]
        print(value)
    elif letter_index > shift and letter_index !=26:
        letter_index = x.index(letter)
        value = x[letter_index - 26 + shift]
        print(value)
    elif letter_index == 26:
        value = " "
        print(value)
    
# shift_letter("A", 0) 
# shift_letter("A", 2)
# shift_letter("Z", 1) 
# shift_letter("X", 5) 
# shift_letter(" ", 5) 

def shift_by_letter(letter, letter_shift): 
    y = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ")
    letter_index = y.index(letter)
    if letter_index == 0:
        new_index = letter_index + y.index(letter_shift)
        value = y[new_index]
        print(value)
    
    elif letter_index != 0 and letter_index != 26:
        new_index = letter_index + y.index(letter_shift)
        value = y[new_index]
        print(value)

    elif letter_index == 26:
        value = " "
        print(value)

shift_by_letter("A", "A")
shift_by_letter("A", "C")
shift_by_letter("B", "K")
shift_by_letter(" ", "K")

