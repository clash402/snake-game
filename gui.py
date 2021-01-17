from turtle import Screen


class GUI():
    def __init__(self):
        self.screen = Screen()

        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game!")
        self.screen.tracer(0)

    # PUBLIC METHODS
    def listen(self):
        self.screen.listen()

    def onkey(self, fn, key):
        self.screen.onkey(fn, key)

    def update(self):
        self.screen.update()

    def exitonclick(self):
        self.screen.exitonclick()
