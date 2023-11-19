# Todo-1 : Combine the encrypt() and decrypt() functions into a single function called caesar().

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
    , 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
    , 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]

def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    # Todo-2: Inside the caesar() function, shift each letter of the 'text' forwards or backwards in the alphabet by
    #  the shift amount depending on the direction and print the encrypted text. e.g. plain_text = "hello" shift = 5
    #  direction = "encode" cipher_text = "mjqqt" print output: "The encoded text is mjqqt"
    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The {cipher_direction}d text is {cipher_text}")


# Todo-3: import and print the logo from art.py when the program starts.
from art import logo

print(logo)

# variable direction for user to choose
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# variable text for user to enter the text
text = input("Type your message:\n").lower()
# variable shift for user to enter the shift number
shift = int(input("Type the shift number:\n"))


# TODO-5: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)
