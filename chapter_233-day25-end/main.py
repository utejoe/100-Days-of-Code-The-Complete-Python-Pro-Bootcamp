import turtle
import pandas
import os

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Get the absolute path to the image file
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, 'blank_states_img.gif')

# Check if the image file exists
if not os.path.exists(image_path):
    print(f"Error: The image file '{image_path}' was not found.")
    exit(1)

screen.addshape(image_path)
turtle.shape(image_path)

# Read the CSV data
csv_path = os.path.join(current_dir, '50_states.csv')

# Check if the CSV file exists
if not os.path.exists(csv_path):
    print(f"Error: The CSV file '{csv_path}' was not found.")
    exit(1)

data = pandas.read_csv(csv_path)
all_states = data.state.to_list()

# List to keep track of guessed states
guessed_states = []

# Main game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center", font=("Arial", 8, "normal"))

# Creating a list of missing states
missing_states = [state for state in all_states if state not in guessed_states]

# Creating a DataFrame from the list of missing states
new_data = pandas.DataFrame(missing_states, columns=["state"])

# Saving the DataFrame to a new CSV file
new_data.to_csv(os.path.join(current_dir, 'states_to_learn.csv'), index=False)

# Keep the screen open until clicked
turtle.mainloop()
