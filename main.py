from gui import GUI
from snake import Snake
from game import Game


# PROPERTIES
gui = GUI()
snake = Snake(gui)
game = Game(gui, snake)


# MAIN
game.play()
gui.exitonclick()
