from turtle import Turtle


class Snake:
    def __init__(self, gui):
        self._UP = 90
        self._DOWN = 270
        self._LEFT = 180
        self._RIGHT = 0

        self.gui = gui
        self._segments = []
        self._segment_size = 20
        self._starting_pos = [(0, 0), (-self._segment_size, 0), (-self._segment_size * 2, 0)]
        self.speed = 0.1

        self._create()
        self._listen_for_movement()

        self._head = self._segments[0]

    # PRIVATE METHODS
    def _create(self):
        for pos in self._starting_pos:
            self._add_segment(pos)

    def _reset(self):
        for segment in self._segments:
            segment.goto(1000, 1000)

        self._segments.clear()
        self._create()
        self._head = self._segments[0]

    def _add_segment(self, pos):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(pos)
        self._segments.append(segment)

    def _extend(self):
        self._add_segment(self._segments[-1].position())

    def _listen_for_movement(self):
        self.gui.listen()
        self.gui.onkey(self._turn_up, "Up")
        self.gui.onkey(self._turn_down, "Down")
        self.gui.onkey(self._turn_left, "Left")
        self.gui.onkey(self._turn_right, "Right")

    def _turn_up(self):
        if self._head.heading() != self._DOWN:
            self._head.setheading(self._UP)

    def _turn_down(self):
        if self._head.heading() != self._UP:
            self._head.setheading(self._DOWN)

    def _turn_left(self):
        if self._head.heading() != self._RIGHT:
            self._head.setheading(self._LEFT)

    def _turn_right(self):
        if self._head.heading() != self._LEFT:
            self._head.setheading(self._RIGHT)

    # PUBLIC METHODS
    def move(self):
        for segment_n in range(len(self._segments) - 1, 0, -1):
            pos_x = self._segments[segment_n - 1].xcor()
            pos_y = self._segments[segment_n - 1].ycor()
            self._segments[segment_n].goto(pos_x, pos_y)

        self._head.forward(self._segment_size)

    def has_eaten(self, food):
        if self._head.distance(food) < 15:
            self._extend()
            return True

    def has_touched_itself(self):
        for segment in self._segments[1:]:
            if self._head.distance(segment) < 10:
                self._reset()
                return True

    def has_left_screen(self):
        if self._head.xcor() > 280 or self._head.xcor() < -280 or self._head.ycor() > 280 or self._head.ycor() < -280:
            self._reset()
            return True
