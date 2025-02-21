from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food(snake)
score = Score()

screen.listen()
screen.onkey(key="d",fun=snake.turn_right)
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="w", fun=snake.turn_up)
screen.onkey(key="s", fun=snake.turn_down)

end = 0
curr_key = ""
food.create_food()
while end == 0:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if food.check_head_pos():
        snake.add_snake()
        score.update_score()
    if snake.check_wall() or snake.check_tail():
        score.game_over()
        screen.exitonclick()



screen.exitonclick()