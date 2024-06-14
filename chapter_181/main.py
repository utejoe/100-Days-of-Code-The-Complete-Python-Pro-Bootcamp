from turtle import Turtle, Screen
import random

# Setup the screen
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")

# Prompt the user for a bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Define the colors and starting positions for the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

# Create the turtles
for index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[index])
    turtles.append(tim)

# Start the race
if user_bet:
    race_on = True
else:
    race_on = False

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:  # Check if any turtle has reached the finish line
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations! You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry, you lost. The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Keep the screen open
screen.exitonclick()
