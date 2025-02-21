from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0,y=250)
        self.hideturtle()
        self.write(f"Score {self.score}", move=False, align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(x=0,y=-200)
        self.write(f"Game Over :(", move=False, align="center", font=FONT)
        self.goto(x=0, y=-250)
        self.write(f"Final Score {self.score}", move=False, align="center", font=FONT)



