from bs4 import BeautifulSoup

# Open the HTML file and read its contents with the correct encoding
with open("website.html", "r", encoding="utf-8") as file:
    contents = file.read()

# Create a BeautifulSoup object by parsing the HTML content
soup = BeautifulSoup(contents, "html.parser")

# Print the entire soup object (the parsed HTML)
print(soup)

# Print the prettified version of the parsed HTML
print(soup.prettify())

# Extract and print the title tag
print(soup.title)

# Extract and print the name of the title tag
print(soup.title.name)

# Extract and print the string within the title tag
print(soup.title.string)

# Extract and print the first anchor tag
print(soup.a)

# Extract and print the first list item tag
print(soup.li)

# Extract and print the first paragraph tag
print(soup.p)
