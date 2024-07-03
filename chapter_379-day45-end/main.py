import requests
from bs4 import BeautifulSoup
import os

# Define the URL for Empire's top 100 movies list
URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

# Fetching HTML from the URL
response = requests.get(URL)
html_content = response.text

# Parsing HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Finding all <h3> elements with specific class (adjusted to the new class name)
all_movies = soup.find_all('h3', class_='listicleItem_listicle-item__title__BfenH')

# Extracting movie titles
movie_titles = [movie.getText().strip() for movie in all_movies]

# Reversing the list to start from 1 down to 100
movies = movie_titles[::-1]

# Get the current directory where this script is located
current_directory = os.path.dirname(__file__)

# Specify the path to the movies.txt file in the current directory
movies_file_path = os.path.join(current_directory, 'movies.txt')

# Writing movie titles to the text file
with open(movies_file_path, 'w') as file:
    for movie in movies:
        file.write(movie + '\n')

# Output confirmation
print(f'Successfully created {movies_file_path} with top 100 movies listed.')
