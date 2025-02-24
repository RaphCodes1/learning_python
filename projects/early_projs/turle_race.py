import random
from turtle import Turtle, Screen

turtles = [Turtle() for _ in range(5)]

turtle_len = len(turtles)
screen = Screen()
screen.setup(height=400,width=500)
screen.bgcolor("black")
screen.title("Turtle Race")
user_bet = screen.textinput(title="Make your bet", prompt = "Enter color")

colors = ["red", "blue", "green", "yellow", "purple"]
start_pos = [-100, -50, 0, 50, 100]
for i, turtle in enumerate(turtles):
    turtle.penup()
    turtle.goto(-230,start_pos[i])
    turtle.color(colors[i])
    turtle.shape("turtle")

end_sim = 0
win_color = ""
while end_sim == 0:

    for i, tur in enumerate(turtles):
        if tur.xcor() >= 230:
            win_color = tur.color()[0]
            print(f"{win_color} Wins!")
            end_sim = 1
            break
        tur.forward(random.randint(0,10))

if user_bet == win_color:
    print("You win!")
else:
    print("You lose :(")
screen.exitonclick()