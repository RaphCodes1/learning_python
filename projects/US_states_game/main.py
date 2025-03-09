import turtle
from turtle import Turtle, Screen
import pandas

FONT = ("Arial",10,"normal")
screen = Screen()
image = "blank_states_img.gif"
screen.setup(height=491, width=725)
screen.title("Guess the states")
screen.addshape(image)
turtle.shape(image)

screen.listen()
screen.onkey(key="Escape",fun=screen.bye)

data = pandas.read_csv("50_states.csv")
states = data.state
x_coord = data.x
y_coord = data.y


def make_turtle(check, x, y, mode):
    new = Turtle()
    new.shape("square")
    new.hideturtle()
    new.penup()
    new.goto(x=x,y=y)
    if mode == "finish":
        new.write(f"{check}", move=False, align="center", font=("Arial",40,"normal"))
    else:
        new.write(f"{check}", move=False, align="center", font=FONT)

states_check = 0
guessed_states = []

while 1:
    user_input = turtle.textinput(f"{states_check}/50 states guessed", prompt="What's another state's name?")
    i = 0
    if user_input is None or user_input == "exit":
        converted = states.to_list()
        missing_states = [s for s in converted if s not in guessed_states]
        out = pandas.DataFrame(missing_states)
        out.to_csv("states_to_learn.csv")
        screen.exitonclick()
        break
    else:
        capital = user_input.title()
    for check in states:
        if capital == check:
            valid = 1
            for guessed in guessed_states:
                if guessed == check:
                    valid = 0
                    break
            if valid == 1:
                make_turtle(check, x_coord[i], y_coord[i],"normal")
                guessed_states.append(check)
                states_check += 1
            break
        i += 1
    if states_check == 50:
        make_turtle("Congratulations! You won!",0,0, "finish")
        screen.exitonclick()
        break

turtle.mainloop()