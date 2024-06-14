# Define a class named User
class User: 
    
    # Initialize the User class with user_id and username attributes
    # and set the followers attribute to 0
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

# Create an instance of the User class with id "001" and username "angela"
user_1 = User("001", "angela")

# Create another instance of the User class with id "002" and username "angela"
user_2 = User("002", "angela")

# Print the username attribute of the user_1 instance
print(user_1.username)

# Print the followers attribute of the user_1 instance
print(user_1.followers)
