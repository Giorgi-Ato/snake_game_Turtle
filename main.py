from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

body_segments = []
x_position = 0
for _ in range(3):
    trt = Turtle(shape='square')
    trt.penup()
    trt.color('white')
    body_segments.append(trt)
    trt.goto(x=x_position, y=0)
    x_position -= 20

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_number in range(len(body_segments) - 1, 0, -1):
        new_x = body_segments[seg_number - 1].xcor()
        new_y = body_segments[seg_number - 1].ycor()
        body_segments[seg_number].goto(new_x, new_y)

    body_segments[0].forward(20)
    body_segments[0].left(90)




screen.exitonclick()
