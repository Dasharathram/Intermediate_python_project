# import colorgram
import random
import turtle
from turtle import Turtle as t, Screen as s
turtle.colormode(255)
colors_rgb_list = [(240, 242, 245), (223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159),
                   (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84),
                   (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90)]

scoop = t()
print(scoop)
scoop.shape("arrow")


#
#
# def color_generator():
#     colors = colorgram.extract("48_001.jpg", 18)
#     colors_rgb_list = []
#     for obj_color in colors:
#         color_rgb = obj_color.rgb
#         final = (color_rgb.r, color_rgb.g, color_rgb.b)
#         return colors_rgb_list.append(final)


def color_picker():
    return random.choice(colors_rgb_list)


# def heirst_painting():
#     i = 0
#     while i < 100:
#         scoop.speed(2)
#         scoop.pensize(20)
#         for j in range(10):
#             scoop.color(color_picker())
#             scoop.forward(1)
#             scoop.up()
#             scoop.forward(50)
#             scoop.down()
#             j += 1
#         scoop.right(90)
#         scoop.up()
#         scoop.forward(50)
#         scoop.right(90)
#         scoop.down()
#         i += 1


def heirst_painting():
    i = 101
    scoop.speed(5)
    scoop.up()
    scoop.hideturtle()
    scoop.setheading(220)
    scoop.forward(300)
    scoop.setheading(0)
    for j in range(1, i):
        scoop.down()
        scoop.dot(20, random.choice(colors_rgb_list))
        scoop.up()
        scoop.forward(50)
        scoop.down()
        if j % 10 == 0:
            scoop.up()
            scoop.left(90)
            scoop.forward(50)
            scoop.left(90)
            scoop.forward(500)
            scoop.setheading(0)




heirst_painting()

my_screen = s()
my_screen.exitonclick()
