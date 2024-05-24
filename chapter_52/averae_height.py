# Input: Heights of students in centimeters stored in a list named `student_heights`.
student_heights = [180, 165, 170, 175, 160]

# Initialize a variable `total_height` to 0 to accumulate heights.
total_height = 0

# Use a for loop to iterate over each height in the `student_heights` list.
for height in student_heights:
    # Inside the loop, add each height to the `total_height`.
    total_height += height

# Print the total height.
print(f"Total height: {total_height}")

# Initialize a variable `number_of_students` to 0 to count students.
number_of_students = 0

# Use another for loop to iterate over each student in the `student_heights` list.
for student in student_heights:
    # Inside the loop, increment `number_of_students` by 1 for each student.
    number_of_students += 1

# Print the number of students.
print(f"Number of students: {number_of_students}")

# Calculate the average height by dividing `total_height` by `number_of_students`.
average_height = total_height / number_of_students

# Round the average height to get a whole number.
average_height = round(average_height)

# Print the average height.
print(f"Average height: {average_height}")
