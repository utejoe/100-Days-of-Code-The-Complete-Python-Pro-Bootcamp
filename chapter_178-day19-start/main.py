from turtle import Turtle, Screen

# Create the turtle and screen objects
tim = Turtle()
screen = Screen()

# Define the function to move the turtle forwards
def move_forwards():
    tim.forward(10)

# Set the screen to listen for e vents
screen.listen()

# Bind the move_forwards function to the space key
screen.onkey(move_forwards, "space")

# Keep the screen open until clicked
screen.exitonclick()
