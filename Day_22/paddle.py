# create paddle class
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



