from turtle import Turtle

STARTING_POSITION = [(0, 0), (0, -20), (0, -40)]
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
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        trt = Turtle(shape='square')
        trt.penup()
        trt.color('white')
        self.body_segments.append(trt)
        trt.goto(position)

    def extend(self):
        self.add_segment(self.body_segments[-1].position())

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

    def reset(self):
        for seg in self.body_segments:
            seg.goto(1000, 1000)
        self.body_segments.clear()
        self.create_snake()
        self.head = self.body_segments[0]
