from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self._ALIGNMENT = "center"
        self._FONT = ("Courier", 21, "normal")

        with open("data.txt") as data:
            self._high_score = int(data.read())

        self._score = 0

        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self._update_display()

    # PRIVATE METHODS
    def _update_display(self):
        self.clear()
        self.write(f"Score: {self._score} High Score: {self._high_score}", align=self._ALIGNMENT, font=self._FONT)

    # PUBLIC METHODS
    def increase_score(self):
        self._score += 1
        self._update_display()

    def reset_score(self):
        if self._score > self._high_score:
            self._high_score = self._score
            with open("data.txt", mode="w") as data:
                data.write(f"{self._high_score}")

        self._score = 0
        self._update_display()

    def display_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=self._ALIGNMENT, font=self._FONT)
