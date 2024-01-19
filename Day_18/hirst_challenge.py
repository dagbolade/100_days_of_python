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
colormode(255) # set the color mode to 255
tim = Turtle()


# draw the spot paining
# def draw_spot_painting():
#     tim.penup()
#     tim.goto(-200, -200)
#     tim.pendown()
#     tim.speed("fastest")
#     for _ in range(10):
#         for _ in range(10):
#             tim.dot(20, random.choice(color_list))
#             tim.penup()
#             tim.forward(50)
#             tim.pendown()
#         tim.penup()
#         tim.goto(-200, tim.ycor() + 50)
#         tim.pendown()
#
#
# draw_spot_painting()

#or
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# set the starting position of the turtle
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# draw the spot painting
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


# create a screen object for the turtle to draw on
screen = Screen()
screen.exitonclick()
