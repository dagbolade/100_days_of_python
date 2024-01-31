# Day 19

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# move the turtle forward
def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    tim.clear()  # clear the screen
    tim.penup()  # pen up
    tim.home()  # go home
    tim.pendown()  # pen down


# start listening to the screen
screen.listen()
# bind the keystroke to the function
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()  # exit on click
