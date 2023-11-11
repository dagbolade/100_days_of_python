# Treasure Island Game
# Display a welcome message
print("Welcome to Treasure Island.")
# Display a welcome message
print("Your mission is to find the treasure.")


# Ask the user to choose between left or right
left_or_right = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ").lower()
# if the user chooses left, ask them to choose between swim or wait
if left_or_right == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a "
                 "boat. Type 'swim' to swim across. ").lower()
    if lake == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one "
                     "blue."
                     "Which colour do you choose? ").lower()
        if door == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")

