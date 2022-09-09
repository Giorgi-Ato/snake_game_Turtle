from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body_segments = []
        self.create_snake()
        self.head = self.body_segments[0]

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
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
