# step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

stages = ['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========
''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========
''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========
''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========
''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========
''', '''
    +---+
    |   |
    O   |
        |
        |
        |
=========
''', '''
    +---+
    |   |
        |
        |
        |
        |
=========

''']

chosen_word = random.choice(word_list)

# TODO-2: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6
print(f"lives: {lives}")

# TODO-3: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to
# guess.
display = []
for letters in chosen_word:
    display.append("_")
print(display)

# TODO-4: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more "_".
# Then you can tell the user they've won.
while "_" in display:
    # TODO-5: - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    # TODO-6: - Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for letters in range(len(chosen_word)):
        if chosen_word[letters] == guess:
            display[letters] = guess

    # TODO-7: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose")
            break
        print(stages[lives])

    # Join all the elements in the list and turn it into a String.
    # Call: print(' '.join(display))
    print(' '.join(display))

    # Check if user has got all letters.
    if "_" not in display:
        print("You win")
        break

    # TODO-8: - Print 'display' and you should see the guessed letter in the correct position and every other letter
    # replace with "_".
    print(display)

    # TODO-9: - Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has
    # remaining.
    # e.g. If the user has 5 lives left, print the 5th stage ASCII art.
    print(stages[lives])
    print(f"lives: {lives}")
