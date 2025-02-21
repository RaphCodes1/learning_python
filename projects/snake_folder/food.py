from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, snake):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("Cyan1")
        self.index_pos = 0
        self.food_pos = [(random.randint(-250, 250), random.randint(-250, 250))]
        self.snake = snake
        self.snake_head = self.snake.head

    def generate_pos(self):
        my_tuple = (random.randint(-250, 250), random.randint(-250, 250))
        self.food_pos.append(my_tuple)
    def check_head_pos(self):
        if (self.snake_head.distance(self.food_pos[self.index_pos][0],
                                     self.food_pos[self.index_pos][1])
                                        < 15):
            self.generate_pos()
            self.index_pos += 1
            self.create_food()
            return 1
        return 0
    def create_food(self):
        self.goto(self.food_pos[self.index_pos])
