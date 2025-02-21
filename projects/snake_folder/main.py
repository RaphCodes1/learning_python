from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(key="d",fun=snake.turn_right)
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="w", fun=snake.turn_up)
screen.onkey(key="s", fun=snake.turn_down)

end = 0
curr_key = ""
while end == 0:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()