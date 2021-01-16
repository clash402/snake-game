from turtle import Turtle


class Snake:
    def __init__(self):
        self.UP = 90
        self.DOWN = 270
        self.LEFT = 180
        self.RIGHT = 0

        self.segments = []
        self.segment_size = 20
        self.starting_pos = [(0, 0), (-self.segment_size, 0), (-self.segment_size * 2, 0)]
        self.speed = 0.1

        self.create()

        self.head = self.segments[0]

    def create(self):
        for pos in self.starting_pos:
            self.add_segment(pos)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)

        self.segments.clear()
        self.create()
        self.head = self.segments[0]

    def add_segment(self, pos):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_n in range(len(self.segments) - 1, 0, -1):
            pos_x = self.segments[segment_n - 1].xcor()
            pos_y = self.segments[segment_n - 1].ycor()
            self.segments[segment_n].goto(pos_x, pos_y)

        self.head.forward(self.segment_size)

    def turn_up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def turn_down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def turn_left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def turn_right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

    def has_eaten(self, food):
        if self.head.distance(food) < 15:
            self.extend()
            return True

    def has_left_screen(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            self.reset()
            return True

    def has_touched_itself(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                self.reset()
                return True
