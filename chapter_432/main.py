# Defining the User class
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

# Defining the is_authenticated_decorator
def is_authenticated_decorator(func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            return func(*args, **kwargs)
        else:
            return "User is not authenticated"
    return wrapper

# Applying the decorator to the create_blog_post function
@is_authenticated_decorator
def create_blog_post(user):
    return f"{user.name} has created a new blog post!"

# Testing the decorator
if __name__ == '__main__':
    # Create a new user
    user = User("Angela")

    # Try to create a blog post without logging in
    print(create_blog_post(user))  # Should print "User is not authenticated"

    # Log in the user
    user.is_logged_in = True

    # Try to create a blog post after logging in
    print(create_blog_post(user))  # Should print "Angela has created a new blog post!"
