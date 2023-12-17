# day 16 about oop
# 100 days of code
# creating an object from a blueprint that has been created
# class is a blueprint, which also means defining the attributes and method
# object is an instance of the class

# the code below is creating an object from the turtle class
# constructing an object from a class

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.color("red")
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.color("blue")
timmy.right(120)
timmy.forward(100)
timmy.right(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)

# creating an object from the screen class
my_screen = Screen()

# attributes of the screen class
print(my_screen.canvheight)
print(my_screen.canvwidth)

# methods of the screen class
my_screen.exitonclick() # this method will close the screen when clicked on

