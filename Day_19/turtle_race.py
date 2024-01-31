# the turtle race game
import random
from turtle import Turtle, Screen

screen = Screen()

# set up the screen with the width and height
screen.setup(width=500, height=400)
is_race_on = False
# get the user input for the bet
user_bet = screen.textinput(title="place your bet", prompt="which turtle do you think will win the race? Enter a "
                                                           "color: ")
# set up the list of turtles
turtles = []

# set up the colors for the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(6):
    # create a turtle
    new_turtle = Turtle(shape="turtle")
    # set the color
    new_turtle.color(colors[i])
    # set the position
    new_turtle.penup()  # pen up so that the turtle doesn't draw a line
    new_turtle.goto(x=-235, y=-100 + i * 40)  # 40 is the height of the turtle, i is the index of the turtle
    # add the turtle to the list
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        # check if the turtle has reached the end
        if turtle.xcor() > 230:
            # stop the game
            is_race_on = False

            winning_color = turtle.pencolor()
            # check if the user has won the bet

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

# add a betting option with user able to win or lose
# add a scoreboard
# add a reset option


