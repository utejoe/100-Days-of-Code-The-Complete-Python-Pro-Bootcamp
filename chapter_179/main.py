from turtle import Turtle, Screen

# Create the turtle and screen objects
tim = Turtle()
screen = Screen()

# Define the function to move the turtle forwards
def move_forwards():
    tim.forward(10)

# Define the function to move the turtle backwards
def move_backwards():
    tim.backward(10)

# Define the function to turn the turtle left
def turn_left():
    tim.left(10)

# Define the function to turn the turtle right
def turn_right():
    tim.right(10)

# Define the function to clear the screen and reset the turtle's position
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Set the screen to listen for events
screen.listen()

# Bind the functions to the respective keys
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")

# Keep the screen open until clicked
screen.exitonclick()
