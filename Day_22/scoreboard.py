from turtle import Turtle
# create the scoreboard class

ALIGNMENT = "center"

FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):  # creating the scoreboard class
    def __init__(self):
        super().__init__()  # super() is used to call the __init__() method of the parent class which is Turtle
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score} ", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

