import pandas as pd

# Create a dictionary
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Convert the dictionary to a DataFrame
student_data_frame = pd.DataFrame(student_dict)

# Print the DataFrame
print(student_data_frame)

# Loop through columns
for key, value in student_data_frame.items():
    print(f"Key: {key}")
    print(f"Value: {value}")

# Loop through rows using iterrows()
for index, row in student_data_frame.iterrows():
    print(f"Index: {index}")
    print(f"Row: {row}")
    print(row.student)
    print(row.score)

# Conditional access to find Angela's score
for index, row in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
