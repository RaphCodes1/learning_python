from turtle import Screen
from pong import Pong
from scoreboard import Score
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
score = Score()
pong_1 = Pong(-360)
pong_2 = Pong(360)
ball = Ball()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.bgcolor("black")

def end_game():
    print("Thank you for playing!")
    screen.bye()
end = 0

screen.listen()
screen.onkey(key="w",fun=pong_1.turn_up)
screen.onkey(key="s",fun=pong_1.turn_down)
screen.onkey(key="Up",fun=pong_2.turn_up)
screen.onkey(key="Down",fun=pong_2.turn_down)
screen.onkey(key="Escape",fun=end_game)

while end == 0:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball_up()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.xcor() == pong_2.head.xcor() - 20
        and ball.distance(pong_2.head) < 80):
        ball.bounce_x()
        score.add_play_2()
    elif (ball.xcor() == pong_1.head.xcor() + 20
            and ball.distance(pong_1.head) < 80):
        ball.bounce_x()
        score.add_play_1()
    if ball.xcor() == 400 or ball.xcor() == -400:
        ball.reset()
    if score.score_1 == 12 or score.score_2 == 12:
        end = 1
score.game_over()
screen.exitonclick()