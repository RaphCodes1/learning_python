from turtle import Turtle

class Pong:
    def __init__(self, side):
        self.side = side
        self.segments = []
        self.create_pong()
        self.head = self.segments[0]

    def create_pong(self):
        pong = Turtle(shape="square")
        pong.shapesize(stretch_wid=5, stretch_len=1)
        pong.speed("fastest")
        pong.color("white")
        pong.penup()
        pong.goto(x=int(self.side), y=0)
        self.segments.append(pong)

    def turn_up(self):
        if self.head.ycor() != 280:
            new_y = self.head.ycor() + 20
            self.head.goto(x=int(self.side), y=new_y)

    def turn_down(self):
        if self.head.ycor() != -280:
            new_y = self.head.ycor() - 20
            self.head.goto(x=int(self.side), y=new_y)