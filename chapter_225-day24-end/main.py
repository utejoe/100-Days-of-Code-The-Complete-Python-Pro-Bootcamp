import os

# Define paths
current_folder = os.path.dirname(os.path.abspath(__file__))
names_file_path = os.path.join(current_folder, "Input", "Names", "invited_names.txt")
template_file_path = os.path.join(current_folder, "Input", "Letters", "starting_letter.txt")
output_folder = os.path.join(current_folder, "Output", "ReadyToSend")

# Read names from invited_names.txt
try:
    with open(names_file_path, "r") as names_file:
        names = names_file.readlines()
except FileNotFoundError:
    print(f"Names file not found: {names_file_path}")
    raise

# Read template letter from starting_letter.txt
try:
    with open(template_file_path, "r") as template_file:
        template_letter = template_file.read()
except FileNotFoundError:
    print(f"Template file not found: {template_file_path}")
    raise

# Placeholder in the template letter to replace
PLACEHOLDER = "[name]"

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

# Generate personalized letters
for name in names:
    stripped_name = name.strip()  # Remove leading/trailing whitespace
    new_letter = template_letter.replace(PLACEHOLDER, stripped_name)

    # Construct filename for each personalized letter
    output_file_path = os.path.join(output_folder, f"letter_for_{stripped_name}.txt")

    # Write the personalized letter to a new file
    with open(output_file_path, "w") as output_file:
        output_file.write(new_letter)

print("All letters have been generated and saved in the ReadyToSend folder.")
