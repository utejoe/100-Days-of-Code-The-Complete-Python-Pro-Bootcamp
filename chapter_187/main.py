# main.py
from turtle import Screen
import time
from snake import Snake

# Create the screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Turn off the screen updates
screen.tracer(0)

# Create a snake object
snake = Snake()

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

# Exit on click
screen.exitonclick()
