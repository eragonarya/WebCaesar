def alphabet_position(char):
    if char >= 97 and char <= 122:
        char -= 97
    elif char >= 65 and char <= 90:
        char -= 65
    return char

def rotate_character(letter,rot):
    if letter < 123 and letter >= 97:
        letter = alphabet_position(letter)
        letter += rot%26
        letter = letter%26
        letter += 97
    elif letter < 91 and letter >= 65:
        letter = alphabet_position(letter)
        letter += rot%26
        letter = letter%26
        letter += 65
    return letter


def rotate(string,length):
    new = ''
    for i in string:
        char = ord(i)
        char = rotate_character(char,length)
        new += chr(char)
    return new
