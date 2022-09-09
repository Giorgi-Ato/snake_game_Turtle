from turtle import Turtle

MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.body_segments = []
        self.create_snake()

    def create_snake(self):
        x_position = 0
        for _ in range(3):
            trt = Turtle(shape='square')
            trt.penup()
            trt.color('white')
            self.body_segments.append(trt)
            trt.goto(x=x_position, y=0)
            x_position -= 20

    def move(self):
        for seg_number in range(len(self.body_segments) - 1, 0, -1):
            new_x = self.body_segments[seg_number - 1].xcor()
            new_y = self.body_segments[seg_number - 1].ycor()
            self.body_segments[seg_number].goto(new_x, new_y)
        self.body_segments[0].forward(MOVE_DISTANCE)
