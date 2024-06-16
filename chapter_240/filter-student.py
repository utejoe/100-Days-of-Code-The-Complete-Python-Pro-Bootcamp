
import random

# List of student names
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddy"]

# Dictionary comprehension to generate random scores for each student
student_scores = {name: random.randint(1, 100) for name in names}

# Dictionary comprehension to filter students who scored 60 or above
passed_students = {student: score for student, score in student_scores.items() if score >= 60}
print(passed_students)  # Output: {'Caroline': score, 'Dave': score, ...} for students who passed
