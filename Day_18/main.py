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
tim.color("dark orange")
for times in range(15):
    tim.forward(10) # move forward 10 pixels
    tim.penup() # lift the pen up
    tim.forward(10) # move forward 10 pixels
    tim.pendown() # put the pen down


# create a screen object for the turtle to draw on
screen = Screen()
screen.exitonclick()
