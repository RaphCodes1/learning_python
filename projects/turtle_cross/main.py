from turtle import Screen
from player import Player
from scoreboard import Score
from obstacle import Obstacle
import time

screen = Screen()
screen.tracer(0)
score = Score()
player = Player()
obstacle = Obstacle()

screen.setup(width=600, height=600)
screen.bgcolor("white")

end = 0

screen.listen()
screen.onkey(key="w", fun=player.move_forward)
screen.onkey(key="s", fun=player.move_backward)
screen.onkey(key="Escape", fun=screen.bye)

move = 10

while end == 0:
    time.sleep(obstacle.move_speed)
    screen.update()
    obstacle.move_obstacles(move)
    if player.ycor() == 270:
        player.reset_turtle()
        score.update_level()
        obstacle.increase_speed()
        move += 1
    if obstacle.detect_collision(player):
        score.game_over()
        screen.exitonclick()
        break

screen.exitonclick()