#day 16: Object_Oriented_Programming (OOP)

# import turtle #(1st way of importing)
# test = turtle.turtles()

# from turtle import Turtle, Screen #(2nd way of importing)
# test = Turtle()
# test.shape("turtle")
# test.color("cyan1")
# test.forward(100)
#
# screen = Screen()
# screen.setup(width=500, height=500)
# screen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Names", ["Raphael", "Moe", "Jerome"])
# table.add_column("Names", ["Raphael", "Moe", "Jerome"])
# table.align = "l"
# print(table)

#day 17: creating own classes
# class User:
#     def __init__(self, name, id_per):
#         self.name = name
#         self.id_per = id_per
#         self.age = 23
#         self.friends = []
#
#     def friends_add(self, person):
#         self.friends.append(person)
#
# Person_1 = User("Raphael","001")
# Person_2 = User("Moe","002")
# Person_1.friends_add(Person_2.name)
# print(Person_1.friends)

#day 18: turtle module and GUI
# def draw_square(angle):
#     test.right(angle)
#     test.forward(100)
#
#
# def dotted_lines():
#     test.forward(10)
#     test.penup()
#     test.forward(10)
#     test.pendown()
#
# def random_walk(direction, l_or_r):
#     angles = [0, 90, 180, 360]
#     getattr(test,l_or_r)(random.choice(angles))
#     getattr(test,direction)(40)
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     my_tuple = (r,g,b)
#     return my_tuple
#
# from turtle import Turtle, Screen
# import random
#
# colors = ["red", "blue", "green", "yellow", "purple",
#           "orange", "pink", "brown"]
#
# direction = ["forward", "backward"]
# l_or_r = ["right", "left"]
# test = Turtle()
# screen = Screen()
# test.shape("turtle")
# test.color("Cyan1")
# screen.colormode(255)
# screen.bgcolor(0, 0, 0)
# test.pensize(10)
# test.speed(5)
# for i in range(100):
#     random_walk(random.choice(direction),random.choice(l_or_r))
#     test.color(random_color())

# length = 3

# for i in range(8):
#     angle = 360 / length
#     for f in range(length):
#         draw_square(angle)
#     length += 1
#     test.color(random.choice(colors))

# screen.exitonclick()

#day 19: Instances, State and Higher Order Functions
# projects sketch app and turtle race









