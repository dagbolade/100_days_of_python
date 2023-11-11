# Treasure Island Game
# Display a welcome message
print("Welcome to Treasure Island.")
# Display a welcome message
print("Your mission is to find the treasure.")
# Ask the user to choose between left or right
left_or_right = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ").lower()
# if the user chooses left, ask them to choose between swim or wait

if left_or_right == "left":
    swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait "
                         "for a boat. Type 'swim' to swim across. ").lower()
    # if the user chooses wait, ask them to choose between red, blue or yellow
    if swim_or_wait == "wait":
        red_blue_yellow = input("You arrive at the island unharmed. There is a house with 3 doors. One red, "
                                "one yellow and one blue. Which colour do you choose? ").lower()
        # if the user chooses red, print "Burned by fire. Game Over."
        if red_blue_yellow == "red":
            print("Burned by fire. Game Over.")
        # if the user chooses blue, print "Eaten by beasts. Game Over."
        elif red_blue_yellow == "blue":
            print("Eaten by beasts. Game Over.")
        # if the user chooses yellow, print "You Win!"
        elif red_blue_yellow == "yellow":
            print("You Win!")
        # if the user chooses anything else, print "Game Over."
        else:
            print("Game Over.")
    # if the user chooses swim, print "Attacked by trout. Game Over."
    else:
        print("Attacked by trout. Game Over.")
# if the user chooses right, print "Fall into a hole. Game Over."
else:
    print("Fall into a hole. Game Over.")
