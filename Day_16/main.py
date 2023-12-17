# day 16 about oop
# 100 days of code
# creating an object from a blueprint that has been created
# class is a blueprint
# object is an instance of the class

# the code below is creating an object from the turtle class
# constructing an object from a class

from turtle import Turtle, Screen

timmy = Turtle()

# creating an object from the screen class
my_screen = Screen()
# tapping into the screen attributes and seeing what they are

print(my_screen.canvheight)
print(my_screen.canvwidth)