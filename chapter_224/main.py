import os

# Get the absolute path of the current script's directory
current_folder = os.path.dirname(os.path.abspath(__file__))

# Define absolute paths for the input and output directories
input_folder = os.path.join(current_folder, "Input", "Letters")
names_file_path = os.path.join(current_folder, "Input", "Names", "invited_names.txt")
output_folder = os.path.join(current_folder, "Output", "ReadyToSend")

# Print paths to debug
print(f"Template file path: {input_folder}")
print(f"Names file path: {names_file_path}")
print(f"Output folder path: {output_folder}")

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

# Read the template letter
template_file_path = os.path.join(input_folder, "starting_letter.txt")
try:
    with open(template_file_path, "r") as template_file:
        template_letter = template_file.read()
except FileNotFoundError:
    print(f"Template file not found: {template_file_path}")
    raise

# Read the list of names
try:
    with open(names_file_path, "r") as names_file:
        names = names_file.readlines()
except FileNotFoundError:
    print(f"Names file not found: {names_file_path}")
    raise

# Generate personalized letters
for name in names:
    stripped_name = name.strip()  # Remove any leading/trailing whitespace
    personalized_letter = template_letter.replace("[name]", stripped_name)
    output_file_path = os.path.join(output_folder, f"letter_for_{stripped_name}.txt")
    
    # Save the personalized letter to the output directory
    with open(output_file_path, "w") as output_file:
        output_file.write(personalized_letter)

print("All letters have been generated and saved in the ReadyToSend folder.")
