from turtle import Turtle, Screen

def move_forward():
    sir.forward(10)

def move_backward():
    sir.backward(10)

def turn_left():
    sir.forward(5)
    new_heading = sir.heading() + 10
    sir.setheading(new_heading)

def turn_right():
    sir.forward(5)
    new_heading = sir.heading() - 10
    sir.setheading(new_heading)


def clear_draw():
    sir.clear()
    sir.penup()
    sir.goto(0,0)
    sir.pendown()

sir = Turtle()
screen = Screen()

sir.shape("turtle")

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_draw)

screen.exitonclick()
