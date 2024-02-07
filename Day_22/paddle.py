# create paddle class
from random import random
from turtle import Turtle


class Paddle(Turtle): # creating the paddle class
    def __init__(self, position):
        super().__init__() # super() is used to call the __init__() method of the parent class which is Turtle
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20 # moving the paddle up
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20 # moving the paddle down
        self.goto(self.xcor(), new_y)

        # Function to control the computer paddle
    def computer_control(self, ball):
        # Generate a random number between 0 and 1
        random_number = random()

        # Adjust this value to change the probability of the computer paddle moving
        # Higher values make the computer paddle more likely to move
        # Lower values make the computer paddle less likely to move
        probability_threshold = 0.6

        # If the random number is below the threshold, move the paddle up
        if random_number < probability_threshold:
            if ball.ycor() > self.ycor():
                self.go_up()

        # If the random number is above the threshold, move the paddle down
        else:
            if ball.ycor() < self.ycor():
                self.go_down()



