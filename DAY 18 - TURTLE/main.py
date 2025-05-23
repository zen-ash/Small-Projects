from turtle import Turtle, Screen

import random

timmy = Turtle()
timmy.shape("triangle")
# timmy.color("red")

# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# for i in range(10):
#     timmy.forward(20)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# SIDE = 3
# for i in range(8):
#     total_angle = 360
#     SIDE
#     angle_of_shape = total_angle/SIDE
#     a = (random.random())
#     b = (random.random())
#     c = (random.random()) 
#     # print(a,b,c)

#     timmy.pencolor(a,b,c)
    
#     for i in range(SIDE):
#         timmy.forward(100)
#         timmy.right(angle_of_shape)
#     SIDE += 1



# def draw_shape(num_of_sides):
#     angle = 360/num_of_sides
#     for i in range(num_of_sides):
#         timmy.forward(100)
#         timmy.right(angle)

def change_color():
    a = random.random()
    b = random.random()
    c = random.random()
    timmy.pencolor(a,b,c)

# def main():
#     num_of_sides = 3
#     while (num_of_sides<=10):
#         change_color()
#         draw_shape(num_of_sides)
#         num_of_sides += 1

# main()

####Random Walk


def move_forward():
    timmy.forward(25)

angle = [0,90,180,270]
timmy.speed('fast')
timmy.pensize('5')


while True:
    random_angle = random.choice(angle)
    change_color()
    timmy.setheading(random_angle)
    move_forward()









screen = Screen()
screen.exitonclick()
