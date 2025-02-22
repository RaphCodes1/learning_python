from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "brown", "magenta"]

class Obstacle:
    def __init__(self):
        self.segments = []
        self.create_obstacles()
        self.move_speed = 0.1

    def create_obstacles(self):
        for i in range(40):
            x_pos = random.randint(-300,300)
            y_pos = random.randint(-220, 300)
            objs = Turtle()
            objs.shape("square")
            objs.shapesize(stretch_wid=0.7, stretch_len=random.uniform(1,1.5))
            objs.color(random.choice(COLORS))
            objs.penup()
            objs.goto(x=x_pos, y=y_pos)
            self.segments.append(objs)

    def move_obstacles(self,move):
        for i in range(0,40):
            y_pos = self.segments[i].ycor()
            new_y = random.randint(-150, 250)
            if self.segments[i].xcor() <= -300:
                self.segments[i].goto(x=400, y=new_y)
            else:
                new_x = self.segments[i].xcor() - move
                self.segments[i].goto(x=new_x,y=y_pos)

    def detect_collision(self, player):
        for i in range(0,40):
            if self.segments[i].distance(player) < 15:
                return 1
        return 0

    def increase_speed(self):
        self.move_speed *= 0.9
