from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 25, 'bold')


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.write(arg= f"Score: {self.score}" , move= False, align= ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg= f"Game Over" , move= False, align= ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()