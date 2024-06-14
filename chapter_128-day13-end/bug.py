# Bug Code: Utilizing Print Statements for Debugging

# Initialize variables
pages = 0
words_per_page = 0

# Take user input for number of pages and words per page
pages = int(input("Enter the number of pages: "))
words_per_page = int(input("Enter the number of words per page: "))

# Calculate total number of words in the book
total_words = pages * words_per_page

# Print the total number of words
print("Total words in the book:", total_words)
