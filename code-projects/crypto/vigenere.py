from helpers import alphabet_position, rotate_character

def encrypt (text, key):
    Alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    secretMessage = ""
    lstOfRots= []
    i = 0
    for char in key:
        rot = alphabet_position (char)
        lstOfRots.append(rot)
        x = len(lstOfRots)
        y = x -1
    for let in text:
        if let not in Alphabet and let not in alphabet:
            secretMessage = secretMessage + let
        else:
            newChar = rotate_character (let, lstOfRots[i])
            secretMessage = secretMessage + newChar
            if i < y:
                i = i +1
            else:
                i = 0
    return secretMessage

def main():
    text = input ("Type a message:")
    key = input ("Encryption key:")
    print (encrypt(text, key))

if __name__ == '__main__':
    main()
