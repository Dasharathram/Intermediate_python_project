import turtle
from turtle import Turtle as t, Screen as s
import random
from heirst_painting import submain

turtle.colormode(255)
scoop = t()
my_screen = s()

print(scoop)
scoop.shape("arrow")
scoop.speed(5)


def color_picker():
    return random.choice(submain.colors_rgb_list)


color_picker()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


list_color = ["chartreuse", "peru", "lime green", "steel blue", "firebrick", "magenta", "sandy brown", "sky blue",
              "black", "olive drab", "dark turquoise"]
for i in range(4):
    scoop.forward(100)
    scoop.left(80)
for _ in range(15):
    scoop.forward(10)
    scoop.penup()
    scoop.forward(10)
    scoop.pendown()


def polygon_draw(move=100, sides=3):
    while sides < 10:
        color = color_picker()
        for side in range(sides):
            scoop.color(color)
            scoop.forward(move)
            angle = 360 / sides
            scoop.right(angle)
        sides += 1


polygon_draw()


def direction_picker():
    d_list = [0, 90, 180, 270]
    return random.choice(d_list)


def random_walk(move=30):
    i = 0
    while i < 200:
        scoop.color(random_color())
        scoop.pensize(15)
        scoop.speed(10)
        scoop.setheading(direction_picker())
        scoop.forward(move)
        i += 1


random_walk()


def randomnum():
    return random.randint(0, 360)


def draw_circles():
    i = 0
    while i < 100:
        scoop.color(random_color())
        scoop.speed("fastest")
        scoop.seth(randomnum())
        scoop.circle(100)

        i += 1


draw_circles()


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        scoop.color(random_color())
        scoop.speed("fastest")
        scoop.circle(100)
        scoop.seth(scoop.heading() + size_of_gap)


draw_spirograph(2)


def move_forwards():
    scoop.forward(20)


def move_right():
    scoop.right(10)


def move_left():
    scoop.left(10)


def draw_circle():
    scoop.circle(100)


def clear():
    scoop.clear()
    scoop.penup()
    scoop.home()
    scoop.down()


my_screen.listen()
my_screen.onkey(move_forwards, "space")
my_screen.onkey(move_right, "Right")
my_screen.onkey(move_right, "Left")
my_screen.onkey(draw_circle, "a")
my_screen.onkey(clear, "c")

my_screen.exitonclick()
