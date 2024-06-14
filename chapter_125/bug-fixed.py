# Fixed Code: Reproducing and Fixing the Error

import random

# List of dice images (emojis)
dice_images = ["🎲", "⚀", "⚁", "⚂", "⚃", "⚅"]

# Generate a random number between 0 and 5 (inclusive)
dice_num = random.randint(0, 5)

# Select a dice image based on the random number
selected_image = dice_images[dice_num]

# Print the selected image
print(selected_image)
