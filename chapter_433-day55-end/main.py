# Define the logging_decorator
def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        # Log the function name and arguments
        print(f"You called {fn.__name__} with args: {args} and kwargs: {kwargs}")
        
        # Call the function and get the result
        result = fn(*args, **kwargs)
        
        # Log the returned result
        print(f"It returned: {result}")
        
        # Return the result
        return result
    return wrapper

# Define the function to be decorated
@logging_decorator
def a_function(*args):
    return sum(args)

# Test the decorated function
if __name__ == '__main__':
    print(a_function(1, 2, 3))  # You called a_function with args: (1, 2, 3) and kwargs: {}
                                # It returned: 6
                                # 6
