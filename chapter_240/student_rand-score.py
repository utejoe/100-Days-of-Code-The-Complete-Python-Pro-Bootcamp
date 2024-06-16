import random

# List of student names
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddy"]

# Dictionary comprehension to generate random scores for each student
student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)  # Output: {'Alex': random_score, 'Beth': random_score, ...}

