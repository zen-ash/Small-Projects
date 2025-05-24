# from turtle import Turtle, 
import turtle
import colors
import random

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.shape("triangle")
timmy.speed('fastest')
timmy.hideturtle()
# timmy.pensize(10)
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

# def change_color():
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     random_color = (r,g,b)
#     # timmy.pencolor(r,g,b)
#     return random_color

# def main():
#     num_of_sides = 3
#     while (num_of_sides<=10):
#         change_color()
#         draw_shape(num_of_sides)
#         num_of_sides += 1

# main()

####Random Walk


# def move_forward():
#     timmy.forward(30)

# angle = [0,90,180,270]

# while True:
#     random_angle = random.choice(angle)
#     timmy.pencolor(change_color())
#     # change_color()
#     timmy.setheading(random_angle)
#     move_forward()


#####SPirograph
# def draw_spirograph(size_of_gap):
#     for i in range(int(360/size_of_gap)):
#         timmy.pencolor(change_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)



# a = True
# while a:
#     timmy.pencolor(change_color())
#     timmy.circle(100)
#     timmy.setheading(timmy.heading() + 5)
#     print(timmy.heading())
#     if timmy.heading() == 0.0:
#         a = False

# draw_spirograph(36)



##################################painting heirs

timmy.teleport(-300,-300)
y_cord = -250

for i in range(10):
    for i in range(10):
        timmy.color(random.choice(colors.color_list))
        timmy.begin_fill()
        timmy.circle(20)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    timmy.teleport(x=-300, y= y_cord)
    y_cord += 50



    
screen = turtle.Screen()
screen.exitonclick()
