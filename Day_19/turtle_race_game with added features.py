import random
from turtle import Turtle, Screen

# Set up the screen with the width and height
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race Betting Game")

# Initialize a dictionary to store player names and their money
players = {}

while True:
    # Get player names only if the dictionary is empty (first game)
    if not players:
        player_name = screen.textinput(title="Enter Your Name", prompt="Enter your name: ")
        if player_name:
            players[player_name] = 1000  # Initialize each player with 1000 virtual dollars

    # Set up the list of turtles and their colors
    turtles = []
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    for i, color in enumerate(colors):
        # Create a turtle
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=-235, y=-100 + i * 40)  # Position the turtles
        turtles.append(new_turtle)

    # Allow the user to place a bet
    user_bet = screen.textinput(title="Place Your Bet", prompt="Which turtle do you think will win the race? Enter a "
                                                               "color: ")
    if user_bet:
        is_race_on = True
    else:
        is_race_on = False

    # Create a scoreboard
    scoreboard = Turtle()
    scoreboard.hideturtle()
    scoreboard.penup()
    scoreboard.goto(0, 170)
    scoreboard.color("black")
    scoreboard.write("Turtle Race", align="center", font=("Arial", 24, "normal"))
    scoreboard.goto(0, 140)
    scoreboard.write("Betting Options:", align="center", font=("Arial", 16, "normal"))
    scoreboard.goto(0, 110)
    scoreboard.write("Player: {} - Money: ${}".format(player_name, players[player_name]), align="center",
                      font=("Arial", 14, "normal"))

    while is_race_on:
        for turtle in turtles:
            # Check if the turtle has reached the end
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()

                # Check if the user has won the bet
                if winning_color == user_bet:
                    players[player_name] += 100  # User wins $100
                    scoreboard.clear()
                    scoreboard.goto(0, 110)
                    scoreboard.write("Player: {} - Money: ${}".format(player_name, players[player_name]), align="center",
                                      font=("Arial", 14, "normal"))
                    screen.update()
                    screen.title("Turtle Race Betting Game - You Win!")
                    screen.bgcolor("lightgreen")
                else:
                    players[player_name] -= 50  # User loses $50
                    scoreboard.clear()
                    scoreboard.goto(0, 110)
                    scoreboard.write("Player: {} - Money: ${}".format(player_name, players[player_name]), align="center",
                                      font=("Arial", 14, "normal"))
                    screen.update()
                    screen.title("Turtle Race Betting Game - You Lose!")
                    screen.bgcolor("red")

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

    # Ask the user if they want to play again
    play_again = screen.textinput(title="Play Again?", prompt="Do you want to play again? (yes/no)").lower()
    screen.clear()
    screen.bgcolor("white")

    if play_again != "yes":
        break

# Print the final amount for each player
for player, money in players.items():
    print(f"{player}: ${money}")

screen.exitonclick()
