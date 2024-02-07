# creating the pong game
from turtle import Turtle, Screen
import time
from Day_22.paddle import Paddle
from Day_22.ball import Ball

screen = Screen()
screen.setup(width=800, height=600)  # setting the screen size
screen.bgcolor("black")  # setting the background color
screen.title("Pong Game")  # setting the title of the window
screen.tracer(0)  # to turn off the animation, because we want to manually update the screen

# assigning the paddle class to a variable
r_paddle = Paddle((350, 0))  # creating the right paddle in a tuple, because the position method in the paddle class
l_paddle = Paddle((-350, 0))  # creating the left paddle
ball = Ball()  # creating the ball

screen.listen()  # to listen to the keyboard inputs

# moving the right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# moving the left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # to slow down the ball
    screen.update()  # updating the screen manually
    ball.move()  # moving the ball

screen.exitonclick()  # to keep the window open until we click on it
