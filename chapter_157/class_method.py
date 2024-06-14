class User: 
    # Initialize the User class with user_id and username attributes
    # and set the followers and following attributes to 0
    def __init__(self, user_id, username):  # Corrected method name from __int__ to __init__
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Method to follow another user
    def follow(self, user):
        user.followers += 1
        self.following += 1

# Create an instance of the User class with id "001" and username "angela"
user_1 = User("001", "angela")

# Create another instance of the User class with id "002" and username "jack"
user_2 = User("002", "jack")

# user_1 follows user_2
user_1.follow(user_2)

# Print the followers and following attributes of user_1 and user_2
print(user_1.followers)  # Should print 0
print(user_1.following)  # Should print 1
print(user_2.followers)  # Should print 1
print(user_2.following)  # Should print 0
