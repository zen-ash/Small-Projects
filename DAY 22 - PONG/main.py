from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time



screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600, startx= 300, starty= 15)
screen.title("pong")
screen.tracer(0)


paddle_r= Paddle((350,0))
paddle_l = Paddle((-350,0))

ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")


game_is_on = True
ball_speed = 0.1
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -300:
        ball.bounce()

    if ball.xcor() > 320 and ball.distance(paddle_r) < 50 or ball.xcor() < -320 and ball.distance(paddle_l) < 50:
        ball.paddle_bounce()

    if ball.xcor() > 400 : #right paddle misses ( left got point)
        score.l_increase()
        ball.reset_position()
        # time.sleep(0.5)


    if ball.xcor() <-400:  #left paddle misses (right got point)
        score.r_increase()
        ball.reset_position()
        # time.sleep(0.5)

    

        

screen.exitonclick()