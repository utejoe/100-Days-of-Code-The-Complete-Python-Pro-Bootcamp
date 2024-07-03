from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def hello():
    return "Hello, World!"

# Ensure the script runs the app
if __name__ == "__main__":
    app.run()

# Print the name attribute
print(__name__)
