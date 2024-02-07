# creating the pong game
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)  # setting the screen size
screen.bgcolor("black")  # setting the background color
screen.title("Pong Game")  # setting the title of the window
screen.tracer(0)  # to turn off the animation, because we want to manually update the screen

# creating the paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)  # setting the size of the paddle
paddle.penup()  # to not draw the line while moving the paddle
paddle.goto(350, 0)  # setting the position of the paddle

screen.listen()  # to listen to the keyboard inputs


# moving the paddle up
def go_up():
    new_y = paddle.ycor() + 20  # getting the current y position and adding 20 to it
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20  # getting the current y position and subtracting 20 from it
    paddle.goto(paddle.xcor(), new_y)


screen.onkey(go_up, "Up")  # moving the paddle up when the up arrow key is pressed
screen.onkey(go_down, "Down")  # moving the paddle down when the down arrow key is pressed

game_is_on = True
while game_is_on:
    screen.update()  # updating the screen manually

screen.exitonclick()  # to keep the window open until we click on it
