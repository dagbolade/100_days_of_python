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
for times in range(3):
    tim.color("dark slate blue")
    tim.forward(100)
    tim.right(120)

# draw a square
for times in range(4):
    tim.color("dark turquoise")
    tim.forward(100)
    tim.right(90)

# draw a pentagon
for times in range(5):
    tim.color("dark violet")
    tim.forward(100)
    tim.right(72)

# draw a hexagon
for times in range(6):
    tim.color("dark olive green")
    tim.forward(100)
    tim.right(60)

# draw a heptagon
for times in range(7):
    tim.color("dark khaki")
    tim.forward(100)
    tim.right(51.4285714)

# draw a octagon
for times in range(8):
    tim.color("dark goldenrod")
    tim.forward(100)
    tim.right(45)

# draw a nonagon
for times in range(9):
    tim.color("dark salmon")
    tim.forward(100)
    tim.right(40)

# draw a decagon
for times in range(10):
    tim.color("dark slate gray")
    tim.forward(100)
    tim.right(36)



# create a screen object for the turtle to draw on
screen = Screen()
screen.exitonclick()
