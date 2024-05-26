# Function definition
import math

def paint_calc(height, width, cover):
    area = height * width
    num_cans = math.ceil(area / cover)
    print(f"You'll need {num_cans} cans of paint.")

# Example inputs
height = 3
width = 9
cover = 5

# Function call with example inputs
paint_calc(height, width, cover)
