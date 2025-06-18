from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 25, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.write(arg=f"{self.lscore} : {self.rscore}", move= False, align= ALIGNMENT, font= FONT)

    def l_increase(self):
        self.lscore += 1
        self.clear()
        self.update_score()
    
    def r_increase(self):
        self.rscore += 1
        self.clear()
        self.update_score()