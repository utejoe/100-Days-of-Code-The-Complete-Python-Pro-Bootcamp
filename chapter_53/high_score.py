# Input: List of scores.
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Initialize a variable `highest_score` to 0 to track the highest score.
highest_score = 0

# Use a for loop to iterate over each score in the `student_scores` list.
for score in student_scores:
    # Check if the current score is greater than the highest score.
    if score > highest_score:
        # If true, update the highest score to the current score.
        highest_score = score

# Print the highest score after the loop completes.
print(f"The highest score in the class is: {highest_score}")
