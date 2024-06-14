# Import the Screen class from the turtle module
from turtle import Screen

# Create a screen object
screen = Screen()

# Set the background color of the screen to black
screen.bgcolor("black")

# Set the width and height of the screen
screen.setup(width=800, height=600)

# Set the title of the screen to "Pong"
screen.title("Pong")

# Keep the screen open until a mouse click is detected
screen.exitonclick()
