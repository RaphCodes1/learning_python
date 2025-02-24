from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(x=0,y=250)
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.clear()
        with open("store_score.txt", mode="r+") as file:
            content = file.read()
        self.write(f"Score {self.score} {content}", move=False, align="center", font=FONT)

    def update_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore += 1
            with open("store_score.txt",mode="r+") as writing:
                writing.write(f"High Score: {self.highscore}")
        self.print_score()

    def game_over(self):
        self.clear()
        self.goto(x=0,y=-200)
        self.write(f"Game Over :(", move=False, align="center", font=FONT)
        self.goto(x=0, y=-250)
        self.write(f"Final Score {self.score}", move=False, align="center", font=FONT)

    def reset_score(self):
        self.score = 0
        self.print_score()




