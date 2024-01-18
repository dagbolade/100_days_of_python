from turtle import Turtle, Screen

# create a new turtle object
tim = Turtle()

# changing the shape of the turtle
tim.shape("turtle")

# changing the color of the turtle
tim.color("orchid")

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for times in range(4):
#     tim.forward(100)
#     tim.right(90)

# draw a dashed line using a for loop and penup and pendown
# tim.color("dark orange")
# for times in range(15):
#     tim.forward(10) # move forward 10 pixels
#     tim.penup() # lift the pen up
#     tim.forward(10) # move forward 10 pixels
#     tim.pendown() # put the pen down
#

# draw a triangle
# for times in range(3):
#     tim.color("dark slate blue")
#     tim.forward(100)
#     tim.right(120)
#
# # draw a square
# for times in range(4):
#     tim.color("dark turquoise")
#     tim.forward(100)
#     tim.right(90)
#
# # draw a pentagon
# for times in range(5):
#     tim.color("dark violet")
#     tim.forward(100)
#     tim.right(72)
#
# # draw a hexagon
# for times in range(6):
#     tim.color("dark olive green")
#     tim.forward(100)
#     tim.right(60)
#
# # draw a heptagon
# for times in range(7):
#     tim.color("dark khaki")
#     tim.forward(100)
#     tim.right(51.4285714)
#
# # draw a octagon
# for times in range(8):
#     tim.color("dark goldenrod")
#     tim.forward(100)
#     tim.right(45)
#
# # draw a nonagon
# for times in range(9):
#     tim.color("dark salmon")
#     tim.forward(100)
#     tim.right(40)
#
# # draw a decagon
# for times in range(10):
#     tim.color("dark slate gray")
#     tim.forward(100)
#     tim.right(36)

colors = ["dark slate blue", "dark turquoise", "dark violet", "dark olive green", "dark khaki", "dark goldenrod",
          "dark salmon", "dark slate gray"]

# # creae a function to draw a shape
# def draw_shape(num_sides):  # num_sides is the number of sides of the shape
#     angle = 360 / num_sides
#     for times in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):  # this will draw a triangle to a decagon
#     tim.color(colors[shape_side_n - 3])
#     draw_shape(shape_side_n)

# draw a random walk
import random

directions = [0, 90, 180, 270, 360]
tim.pensize(10)
tim.speed("fastest")


def random_walk():
    tim.color(random.choice(colors))  # choose a random color from the colors list
    tim.forward(30)
    tim.setheading(random.choice(directions))  # choose a random direction from the directions list


for _ in range(200):
    random_walk()

# create a screen object for the turtle to draw on
screen = Screen()
screen.exitonclick()
