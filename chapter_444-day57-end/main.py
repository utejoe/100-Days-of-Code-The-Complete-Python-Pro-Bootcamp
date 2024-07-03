from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    # URL of the JSON bin
    blog_url = 'https://api.jsonbin.io/v3/qs/66857a4de41b4d34e40c9de7'  # Replace 'your-bin-id' with your actual bin ID
    response = requests.get(blog_url)
    data = response.json()
    all_posts = data['record']  # Extract the list of posts from the 'record' key
    print(all_posts)  # Print to check structure
    
    return render_template('blog.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)
