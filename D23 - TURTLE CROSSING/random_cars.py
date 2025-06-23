from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10
X_POS = 400
FINAL_POS = -400

class Cars(Turtle):

    def __init__(self,speed):
        super().__init__()
        self.create_cars()
        self.car_speed = speed





    def create_cars(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len= 3, stretch_wid= 1)
        y_pos = random.randint(-200, 200)
        self.penup()
        self.goto(X_POS, y_pos)

    
    def move(self):
        self.backward(self.car_speed)

    def level_up(self):
        self.car_speed +=5 









