from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.reset_turtle()

    def move_forward(self):
        self.forward(10)

    def move_backward(self):
        self.backward(10)

    def reset_turtle(self):
        self.goto(x=0, y=-260)
