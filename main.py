from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")

x_position = 0
for _ in range(3):
    trt = Turtle(shape='square')
    trt.penup()
    trt.color('white')
    trt.goto(x=x_position, y=0)
    x_position -= 20


screen.exitonclick()
