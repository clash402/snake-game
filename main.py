from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# PROPERTIES
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


# MAIN
screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_in_progress = True

while game_is_in_progress:
    screen.update()
    time.sleep(snake.speed)
    snake.move()

    if snake.has_eaten(food):
        food.place()
        scoreboard.increase_score()

    if snake.has_left_screen():
        # game_in_progress = False
        # scoreboard.display_game_over()
        scoreboard.reset_score()

    if snake.has_touched_itself():
        # game_in_progress = False
        # scoreboard.display_game_over()
        scoreboard.reset_score()

screen.exitonclick()
