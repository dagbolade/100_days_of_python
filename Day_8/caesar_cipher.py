# caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
    , 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
    , 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]

# variable direction for user to choose
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# variable text for user to enter the text
text = input("Type your message:\n").lower()
# variable shift for user to enter the shift number
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    # Todo-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    # e.g.  plain_text = "hello" shift = 5 cipher_text = "mjqqt" print output: "The encoded text is mjqqt"
    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print("The encoded text is " + cipher_text)


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

# Todo-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypts(cipher_text, shift_amount):
    plain_text = ""
    # Todo-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
    #  amount and print the decrypted text.
    # e.g.  cipher_text = "mjqqt" shift = 5 plain_text = "hello" print output: "The decoded text is hello"
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print("The decoded text is " + plain_text)


# TODO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call
#  the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND*
#  decrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypts(cipher_text=text, shift_amount=shift)
else:
    print("Invalid input")
