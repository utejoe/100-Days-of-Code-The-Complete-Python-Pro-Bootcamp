from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

@app.route('/greet/<username>')
def greet(username):
    return f'Hello, {username}!'

@app.route('/user/<username>/<int:user_id>')
def show_user(username, user_id):
    return f'Username: {username}, User ID: {user_id}'

@app.route('/file/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath: {subpath}'

if __name__ == '__main__':
    app.run(debug=True)
