from bs4 import BeautifulSoup

# Open the HTML file and read its contents with UTF-8 encoding
with open("website.html", "r", encoding="utf-8") as file:
    contents = file.read()

# Create a BeautifulSoup object by parsing the HTML content
soup = BeautifulSoup(contents, "html.parser")

# Use find_all to get all anchor tags
all_anchor_tags = soup.find_all("a")
print(all_anchor_tags)

# Loop through all anchor tags and get their text
for tag in all_anchor_tags:
    print(tag.getText())

# Get all href attributes from anchor tags
for tag in all_anchor_tags:
    print(tag.get("href"))

# Use find to get an element by ID
heading = soup.find("h1", id="name")
print(heading)

# Use find to get an element by class
section_heading = soup.find("h3", class_="heading")
print(section_heading)

# Use CSS selectors with select_one to get a specific anchor tag
company_url = soup.select_one("p a")
print(company_url)

# Use CSS selectors with select to get all elements with class "heading"
headings_with_class = soup.select(".heading")
print(headings_with_class)
