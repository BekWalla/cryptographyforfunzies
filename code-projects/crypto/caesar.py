from helpers import alphabet_position, rotate_character
from sys import argv
import sys


def user_input_is_valid(cl_args):
    if len(cl_args)>1:
        num = cl_args[1]
        if num.isdigit()==True:
            num = int(num)
            rot = num
            text = input("Please enter a message:")
            return (encrypt(text, rot))
        else:
            return ("Please enter an integer after the program call.")
            sys.exit()
    else:
        return ("Please enter an integer after the program call.")
        sys.exit()

def encrypt (text, rot):
    secretMessage = ""
    for char in text:
        newChar = rotate_character (char, rot)
        secretMessage = secretMessage + newChar
    return secretMessage

def main():
    print (user_input_is_valid (argv))

if __name__ == '__main__':
    main()
