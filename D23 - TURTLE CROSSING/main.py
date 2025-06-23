from turtle import Turtle, Screen
import time
from tim_turtle import Tim
from random_cars import Cars
from scorecard import Score
import random


screen = Screen()
screen.bgcolor("white")
screen.setup(width=800, height= 600)
screen.listen()
screen.tracer(0)

score = Score()
tim = Tim()
screen.onkey(fun=tim.go_up, key="Up")
# screen.onkey(fun=tim.go_down, key="Down")
screen.onkey(screen.bye,     "q")


lst_cars = []
cars_spawned = 0
current_speed = 5      

spawn_rate = 6
game_is_on = True
speed = 0.1

while game_is_on:
    time.sleep(speed)
    screen.update()

    cars_spawned += 1
    if cars_spawned % spawn_rate == 0:


        lst_cars.append(Cars(current_speed))

    for car in lst_cars[:]:
        car.move()
        if car.xcor() < -420:
            car.hideturtle()
            lst_cars.remove(car)

        
        #Collision
        if tim.distance(car) < 20: 
            score.game_over()
            game_is_on = False

    #Detect successfull crossing
    if tim.ycor() > 280:
        tim.reset_pos()
        score.increase_score()
        current_speed += 5
        spawn_rate = max(1, spawn_rate - 1)

        for car in lst_cars:
            car.level_up()

    
    




screen.exitonclick()








