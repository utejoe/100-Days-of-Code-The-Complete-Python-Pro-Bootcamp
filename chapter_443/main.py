from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess/<name>')
def guess(name):
    # Capitalize the first letter of the name
    person_name = name.title()
    
    # Query Genderize API
    gender_url = f"https://api.genderize.io?name={person_name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json() 
    gender = gender_data.get('gender', 'Not Found')
    
    # Query Agify API
    age_url = f"https://api.agify.io?name={person_name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data.get('age', 'Not Found')
    
    return render_template('guess.html', person_name=person_name, gender=gender, age=age)

if __name__ == '__main__':
    app.run(debug=True)
