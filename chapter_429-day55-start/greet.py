from flask import Flask

app = Flask(__name__)

@app.route('/greet/<username>')
def greet(username):
    return f'Hello, {username}!'

if __name__ == '__main__':
    app.run(debug=True)
