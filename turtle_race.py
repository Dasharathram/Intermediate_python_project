import turtle
import random

my_racetrack = turtle.Screen()
my_racetrack.setup(500, 400)
is_race_on = False
user_bet = my_racetrack.textinput(title="Make your bet", prompt="What is the color of your turtle?: ")

colors = ["red", "yellow", "green", "orange", "blue", "purple"]
y_positions = [-120, -70, -20, 30, 80, 130]

all_turtles_list = []
for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.up()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles_list.append(new_turtle)


def winner_decider(color, bet):
    if color == bet:
        print(f"You have won, the {turtle.pencolor()} turtle!!!!")
    else:
        print(f"You lose, the winning turtle is {turtle.pencolor()}!!!!")


if user_bet:
    is_race_on = True
    while is_race_on:
        for turtle in all_turtles_list:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                winner_decider(winning_color, user_bet)
            movement = random.randint(0, 10)
            turtle.forward(movement)

my_racetrack.exitonclick()
