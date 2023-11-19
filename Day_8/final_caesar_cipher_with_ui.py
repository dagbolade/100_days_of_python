alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
    , 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
    , 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]


def caear(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in plain_text:
        # todo-3: what happens if the user enters a number/symbol/space?
        # can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3" end_text = "•••• •• •• 3"
        if letter not in alphabet:
            cipher_text += letter
            continue
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The {cipher_direction}d text is {cipher_text}")


# Todo-1 : import and print the logo from art.py when the program starts.
from art import logo

print(logo)

# todo-4: can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_continue = True
while should_continue:
    # variable direction for user to choose
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # variable text for user to enter the text
    text = input("Type your message:\n").lower()
    # variable shift for user to enter the shift number
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    # TODO-5: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caear(plain_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")

# Todo-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).
