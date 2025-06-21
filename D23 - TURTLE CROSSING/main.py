from turtle import Turtle, Screen
from tim_turtle import Tim
from random_cars import Cars

screen = Screen()
screen.bgcolor("white")
screen.setup(width=800, height= 600)
screen.listen()

tim = Tim()
screen.onkey(fun=tim.go_up, key="Up")
screen.onkey(fun= tim.go_up, key= "w")


game_is_on = True

while game_is_on:
    car = Cars()
    car.move_to_left()














screen.exitonclick()