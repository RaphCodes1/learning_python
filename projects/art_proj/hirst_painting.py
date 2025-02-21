import random
# import colorgram
from turtle import Turtle, Screen

# colors = colorgram.extract('reference.png', 20)
# reference = []
# for i in range(20):
#     reference.append((colors[i].rgb.r,
#         colors[i].rgb.g,colors[i].rgb.b))
#
# for i in range(4):
#     reference.remove(reference[0])
# print(reference)

colors = [(203, 159, 85), (60, 89, 128), (143, 89, 44), (220, 203, 115), (130, 169, 195),
          (149, 55, 85), (44, 56, 104), (124, 34, 48), (139, 186, 146),
          (167, 158, 47), (79, 26, 45), (182, 144, 171), (177, 99, 110),
          (43, 42, 60), (185, 86, 79), (56, 39, 33)]
painting = Turtle()
screen = Screen()

painting.pensize(20)
screen.colormode(255)
screen.setup(width=1000, height=1000)
screen.bgcolor("white")
painting.speed("fastest")
height = (screen.window_height() / 2) - 100
width = (screen.window_width() / 2) - 100
add_h = ((screen.window_height() / 2) * -1) + 50
print(add_h)
while add_h <= height:
    painting.penup()
    painting.goto(-460,add_h + 50)
    add_w = ((screen.window_width() / 2) * -1) + 140
    while add_w <= width:
        painting.color(random.choice(colors))
        painting.penup()
        painting.forward((width / 10) * 2)
        painting.pendown()
        painting.forward(1)
        add_w += width / 10 * 2
    add_h += 90

screen.exitonclick()
