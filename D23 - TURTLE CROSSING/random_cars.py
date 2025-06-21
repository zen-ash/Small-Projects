from turtle import Turtle
import random
X_POS = 400
FINAL_POS = -400

class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.create_cars()




    def create_cars(self):
        self.shape("square")
        self.shapesize(stretch_len= 3, stretch_wid= 1)
        y_pos = random.randint(-200, 200)
        # self.penup()
        self.goto(X_POS, y_pos)

    
    def move_to_left(self):
        while self.xcor() > FINAL_POS:
            move = random.randint(20,30)
            self.backward(move)