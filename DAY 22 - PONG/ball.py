from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.create_ball()




    def create_ball(self):
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1
        

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    
    def bounce(self):
        self.ymove *= -1


    def paddle_bounce(self):
        self.xmove *= -1
        self.move_speed *= 0.9


    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.xmove *=-1
        self.ymove *= -1
