# main.py
from turtle import Screen
import time
from snake import Snake
from food import Food 

# Create the screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Turn off the screen updates
screen.tracer(0)

# Create a snake object
snake = Snake()
food = Food()

# Listen for key presses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        print("Nom Nom Nom")

# Exit on click
screen.exitonclick()


