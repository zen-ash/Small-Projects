from turtle import Turtle


class Tim(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(0,-250)


    def go_up(self):
        self.forward(20)
