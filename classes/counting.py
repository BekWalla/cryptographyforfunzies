alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
letter_count = {}
def counting(sentence):
    for char in sentence:
        if char in alphabet:
                if char in letter_count:
                    letter_count[char]= letter_count[char] + 1
                else:
                    letter_count[char] = 1
    keys = letter_count.keys()
    for char in keys:
        print (char, letter_count[char])

crazy_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."

print (counting(crazy_string))
