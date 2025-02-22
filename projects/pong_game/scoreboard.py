from turtle import Turtle
END_SCORE = 5
FONT = ("Courier", 50, "normal")


def line_middle():
    line = Turtle(shape="square")
    line.hideturtle()
    line.speed("fastest")
    line.setheading(270)
    line.color("white")
    line.penup()
    line.goto(x=0, y=355)
    line.pensize(5)
    for i in range(355, -355, -20):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(20)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.score_1 = 0
        self.score_2 = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=200)
        self.hideturtle()
        self.write(f"{self.score_1} {self.score_2}", move=False,
                    align="center",font=FONT)
        line_middle()

    def add_play_1(self):
        self.score_1 += 1
        self.clear()
        self.write(f"{self.score_1} {self.score_2}", move=False,
                   align="center", font=FONT)


    def add_play_2(self):
        self.score_2 += 1
        self.clear()
        self.write(f"{self.score_1} {self.score_2}", move=False,
                   align="center", font=FONT)

    def game_over(self):
        end = Turtle(shape="circle")
        end.hideturtle()
        end.color("white")
        end.penup()
        end.goto(20,0)
        if self.score_2 == END_SCORE:
            end.write("Game Over!\n Player 2 Wins!",move=False,align="center",font=FONT)
        elif self.score_1 == END_SCORE:
            end.write("Game Over!\n Player 1 Wins!", move=False, align="center", font=FONT)
