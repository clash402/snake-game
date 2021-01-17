from food import Food
from scoreboard import Scoreboard
import time


class Game:
    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake
        self.food = Food()
        self.scoreboard = Scoreboard()

    # PUBLIC METHODS
    def play(self):
        game_is_in_progress = True

        while game_is_in_progress:
            self.screen.update()
            time.sleep(self.snake.speed)
            self.snake.move()

            if self.snake.has_eaten(self.food):
                self.food.place()
                self.scoreboard.increase_score()

            if self.snake.has_left_screen():
                self.scoreboard.reset_score()

            if self.snake.has_touched_itself():
                self.scoreboard.reset_score()
