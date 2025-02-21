from turtle import Turtle

#constants
SET_POS = [0, -20, -40]
MOVE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(0, 3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(x=SET_POS[i], y=0)
            self.segments.append(snake)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[i - 1].xcor()
            y_pos = self.segments[i - 1].ycor()
            self.segments[i].goto(x=x_pos, y=y_pos)
        self.segments[0].forward(MOVE)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
