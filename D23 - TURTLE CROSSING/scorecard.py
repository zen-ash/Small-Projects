
from turtle import Turtle
FONT = ("Courier", 24, "normal")
SCORE_POS = (-280,250)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(SCORE_POS)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(arg= f"Level : {self.score}", move= False, align= "center", font= FONT)

    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,200)
        self.write(f"GAME OVER", align="center", font=FONT)



