import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

screen = Screen()
screen.screensize(500,500)
screen.title("Turtle Race")
screen.bgcolor("lightblue")


def create_turtle():
    t1 = Turtle(shape="turtle")
    t1.shapesize(2,2)
    t1.speed("fastest")
    return t1


color_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

lst_turtle = []


def all_turtle():
    x = -300
    y=-100

    for i in range(0,6):
        tim = create_turtle()
        # tim.color(random.choice(color_list))
        tim.color(color_list[i])
        tim.penup()
        tim.goto(x,y)
        lst_turtle.append(tim)
        y += 40
    



def race():
    all_turtle()
    race_win_bet = screen.textinput("Race","Who will WIN ?").lower()
    while True:
        for i in lst_turtle:
            i.forward(random.randrange(1,11))
            # print(i.xcor())
            if i.xcor() >= 240:
                if i.color()[0] == race_win_bet:
                    print(i.color()[0] + " won the Race. You win")
                else:
                    print(i.color()[0] + " won the Race. You lost")
                return False


race()
# print(lst_turtle)











screen.exitonclick()


