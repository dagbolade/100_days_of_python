# create the ball class
from turtle import Turtle


class Ball(Turtle):  # creating the ball class
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10  # to move the ball 10 pixels to the right
        self.y_move = 10  # to move the ball 10 pixels up


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        print(f"move: {self.x_move}")
        print(f"move: {self.y_move}")


    def bounce_y(self):
        self.y_move *= -1 # to reverse the direction of the ball when it hits the wall
        print(f"bounce_y: {self.y_move}")

    def bounce_x(self):
        self.x_move *= -1
        # to reverse the direction of the ball when it hits the paddle
        print(f"bounce_x: {self.x_move}")

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()



