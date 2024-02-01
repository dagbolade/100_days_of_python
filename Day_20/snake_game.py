import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)  # set up the screen with the width and height
screen.bgcolor("black")  # set the background color to black
screen.title("Snake Game")  # set the title of the screen to Snake Game
screen.tracer(0)  # turn off the animation

starting_positions = [(0, 0), (-20, 0), (-40, 0)]  # set up the starting positions of the snake
segments = []  # initialize the segment list
# create a snake body
for position in starting_positions:
    new_segment = Turtle(shape="square")  # create a new segment
    new_segment.color("white")  # set the color of the segment to white
    new_segment.penup()  # pen up so that the turtle doesn't draw a line
    new_segment.goto(position)  # set the position of the segment
    segments.append(new_segment)  # add the segment to the segment list

# move the snake
game_is_on = True
while game_is_on:
    screen.update()  # update the screen
    time.sleep(0.1)  # sleep for 1 second
    # for segment in segments:
    #     segment.forward(20)  # move the segment forward
    for seg_num in range(len(segments) - 1, 0, -1):  # start from the last segment
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)  # move the first segment forward
    segments[0].right(90)  # turn left



screen.exitonclick()
