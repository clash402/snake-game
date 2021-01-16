from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.ALIGNMENT = "center"
        self.FONT = ("Courier", 21, "normal")

        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.score = 0

        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=self.ALIGNMENT, font=self.FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update()

    def display_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=self.ALIGNMENT, font=self.FONT)
