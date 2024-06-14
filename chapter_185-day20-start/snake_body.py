from turtle import Screen, Turtle

# Create a new screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic screen updates



# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SEGMENT_SIZE = 20

# Create the snake body using a list of positions
segments = []

for position in STARTING_POSITIONS:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

screen.exitonclick()