from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        self.level = 0
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-220, 270)
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.pendown()
        self.write("GAME OVER", align="center", font=FONT)
