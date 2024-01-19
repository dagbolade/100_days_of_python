import random
from turtle import Turtle, Screen, colormode

# import colorgram
#
# colors = colorgram.extract('download.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r # get the red value from the colorgram color
#     g = color.rgb.g # get the green value from the colorgram color
#     b = color.rgb.b # get the blue value from the colorgram color
#
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(239, 231, 235), (227, 236, 230), (198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50),
              (132, 28, 53), (219, 205, 120), (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53),
              (184, 141, 158), (132, 182, 145), (48, 56, 99), (180, 97, 107), (56, 35, 22), (68, 130, 106),
              (98, 118, 166), (82, 148, 159), (221, 175, 187), (169, 206, 166), (90, 151, 96), (185, 97, 80),
              (163, 200, 213), (179, 188, 211), (80, 70, 39), (131, 37, 27)]
# Convert color sequences from range 0-255 to 0-1
colormode(255)  # set the color mode to 255
tim = Turtle()

# draw the spot paining
# def draw_spot_painting():
#     tim.penup() # lift the pen up
#     tim.goto(-200, -200) # move the turtle to the starting position
#     tim.pendown() # put the pen down
#     tim.speed("fastest") # set the speed of the turtle to fastest
#     for _ in range(10): # repeat the following code 10 times
#         for _ in range(10): # repeat the following code 10 times
#             tim.dot(20, random.choice(color_list)) # draw a dot with a random color from the color list
#             tim.penup() # lift the pen up
#             tim.forward(50) # move the turtle forward 50 pixels
#             tim.pendown() # put the pen down
#         tim.penup() # lift the pen up
#         tim.goto(-200, tim.ycor() + 50) # move the turtle to the next row of dots
#         tim.pendown() # put the pen down
#
#
# draw_spot_painting()

# or and alternative way to draw the spot painting and add name "david" drawn by the turtle
def draw_spot_painting():
    tim.penup()  # lift the pen up
    tim.goto(-200, -200)  # move the turtle to the starting position
    tim.pendown()  # put the pen down
    tim.speed("fastest")  # set the speed of the turtle to fastest
    for _ in range(10):  # repeat the following code 10 times
        for _ in range(10):  # repeat the following code 10 times
            tim.dot(20, random.choice(color_list))  # draw a dot with a random color from the color list
            tim.penup()  # lift the pen up
            tim.forward(50)  # move the turtle forward 50 pixels
            tim.pendown()  # put the pen down
        tim.penup()  # lift the pen up
        tim.goto(-200, tim.ycor() + 50)  # move the turtle to the next row of dots
        tim.pendown()  # put the pen down

    tim.penup() # lift the pen up
    tim.goto(-200, 0) # move the turtle to the starting position
    tim.pendown() # put the pen down
    tim.color("dark slate blue") # set the color of the turtle to dark slate blue


draw_spot_painting()

# # draw the spot painting with a different approach

# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
#
# # set the starting position of the turtle
# tim.setheading(225) # set the heading of the turtle to 225
# tim.forward(300) # move the turtle forward 300 pixels
# tim.setheading(0) # set the heading of the turtle to 0
#
# # draw the spot painting
# number_of_dots = 100 # set the number of dots to 100
#
# for dot_count in range(1, number_of_dots + 1): # repeat the following code 100 times
#     tim.dot(20, random.choice(color_list)) # draw a dot with a random color from the color list
#     tim.forward(50) # move the turtle forward 50 pixels
#
#     if dot_count % 10 == 0: # if the dot count is divisible by 10
#         tim.setheading(90) # set the heading of the turtle to 90
#         tim.forward(50) # move the turtle forward 50 pixels
#         tim.setheading(180) # set the heading of the turtle to 180
#         tim.forward(500) # move the turtle forward 500 pixels
#         tim.setheading(0) # set the heading of the turtle to 0

# add a title to the screen
screen = Screen()
screen.title("Hirst Spot Painting")
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor("black")

screen.exitonclick()
