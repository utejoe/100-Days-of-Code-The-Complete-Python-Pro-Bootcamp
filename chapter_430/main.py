from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1 style="text-align: center; color: blue;">Welcome to Uyi's Website!</h1>
    <p style="font-size: 18px;">This is a simple paragraph.</p>
    <img src="https://placekitten.com/200/300" alt="Cute kitten" style="width:200px;">
    <img src='https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif' alt='Cute gif' style='width:200px;'>
    '''

if __name__ == '__main__':
    app.run(debug=True)
