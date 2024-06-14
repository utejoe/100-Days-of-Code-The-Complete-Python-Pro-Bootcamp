from turtle import Screen, Turtle
import time

# Create the screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Turn off the screen updates
screen.tracer(0)

# Create the initial snake body segments
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

# Function to move the snake forward
def move_snake():
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    move_snake()
    time.sleep(0.1)

# Exit on click
screen.exitonclick()
