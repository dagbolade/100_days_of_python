import random
from turtle import Turtle


# create class food and inherit from Turtle

class Food(Turtle): # inherit from Turtle
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5) # stretch the food, make it small
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)  # generate a random x coordinate for the food
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)  # set the position of the food to the center of the screen


