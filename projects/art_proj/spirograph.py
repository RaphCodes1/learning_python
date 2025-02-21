import random
from turtle import Turtle, Screen

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r,g,b)
    return my_tuple

spiro = Turtle()
spiro.speed("fastest")
spiro.pensize(3)
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
def draw_spirograph(tilt):
    for i in range(int(360/tilt) * 2):
        spiro.color(random_color())
        spiro.circle(50)
        spiro.setheading(spiro.heading() + tilt)

draw_spirograph(10)
screen.exitonclick()