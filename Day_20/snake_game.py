# main file for the snake game

import time
from turtle import Screen
from snake import Snake

from food import Food

screen = Screen()
screen.setup(width=600, height=600)  # set up the screen with the width and height
screen.bgcolor("black")  # set the background color to black
screen.title("Snake Game")  # set the title of the screen to Snake Game
screen.tracer(0)  # turn off the animation

snake = Snake()  # create an instance of the snake class for the snake
food = Food()  # create an instance of the food class for the food

screen.listen()  # start listening to the screen
screen.onkey(snake.up, "Up")  # move the snake up when the up arrow key is pressed
screen.onkey(snake.down, "Down")  # move the snake down when the down arrow key is pressed
screen.onkey(snake.left, "Left")  # move the snake left when the left arrow key is pressed
screen.onkey(snake.right, "Right")  # move the snake right when the right arrow key is pressed
# move the snake
game_is_on = True
while game_is_on:
    screen.update()  # update the screen
    time.sleep(0.1)  # sleep for 1 second
    # for segment in segments:
    #     segment.forward(20)  # move the segment forward
    snake.move()

    # detect collision with food and snake
    if snake.head.distance(food) < 15:
        food.refresh()  # refresh the food

screen.exitonclick()  # exit the screen when clicked



