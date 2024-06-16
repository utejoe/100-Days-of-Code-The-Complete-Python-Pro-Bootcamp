# Step 1: Read the contents of both files
with open('file1.txt') as file1:
    list1 = file1.readlines()

with open('file2.txt') as file2:
    list2 = file2.readlines()

# Step 2: Convert the lists of strings to lists of integers
numbers1 = [int(num.strip()) for num in list1]
numbers2 = [int(num.strip()) for num in list2]

# Step 3: Find common numbers using list comprehension
result = [num for num in numbers1 if num in numbers2]

# Print the result to check the code
print(result)
