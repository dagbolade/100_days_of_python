# creating the pong game
from turtle import Turtle, Screen
import time
from Day_22.paddle import Paddle
from Day_22.ball import Ball
from Day_22.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)  # setting the screen size
screen.bgcolor("black")  # setting the background color
screen.title("Pong Game")  # setting the title of the window
screen.tracer(0)  # to turn off the animation, because we want to manually update the screen

# assigning the paddle class to a variable
r_paddle = Paddle((350, 0))  # creating the right paddle in a tuple, because the position method in the paddle class
l_paddle = Paddle((-350, 0))  # creating the left paddle
ball = Ball()  # creating the ball
scoreboard = Scoreboard()  # creating the scoreboard

screen.listen()  # to listen to the keyboard inputs

# moving the right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# moving the left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # to slow down the ball
    screen.update()  # updating the screen manually
    ball.move()  # moving the ball

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # to bounce the ball when it hits the wall

    # detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()  # to bounce the ball when it hits the paddle, 50 is the distance between the ball and the
        # paddle

    # detect when the ball goes out of bounds, R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:  # detect when the ball goes out of bounds, L paddle misses
        ball.reset_position()  # to reset the position of the ball
        scoreboard.r_point()


# when any of the score reaches 5, the game is over, the winner is displayed
    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        print("Game Over, the winner is:" + " " + "Left Paddle" if scoreboard.l_score == 5 else "Right Paddle"
              if scoreboard.r_score == 5 else "No winner")
        game_is_on = False
        scoreboard.game_over()




screen.exitonclick()  # to keep the window open until we click on it
