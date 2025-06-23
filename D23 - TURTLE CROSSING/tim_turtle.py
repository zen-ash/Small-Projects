from turtle import Turtle
STARTING_POS = (0,-250)


class Tim(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(STARTING_POS)


    def go_up(self):
        self.forward(20)

    # def go_down(self):
    #     self.backward(20)

    def reset_pos(self):
        self.goto(STARTING_POS)

    
    
