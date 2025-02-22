from turtle import Turtle
FONT = ("Courier", 25, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=-270, y=240)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def update_level(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        msg = Turtle()
        msg.hideturtle()
        msg.color("black")
        msg.hideturtle()
        msg.penup()
        msg.goto(0,0)
        msg.write("GAME OVER", move=False, align="center",font=FONT)