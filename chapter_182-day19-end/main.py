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
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    turtles.append(new_turtle)

# Start the race
is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:  # Check if any turtle has reached the finish line
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations! You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry, you lost. The {winning_color} turtle is the winner!")
            break

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Keep the screen open
screen.exitonclick()
