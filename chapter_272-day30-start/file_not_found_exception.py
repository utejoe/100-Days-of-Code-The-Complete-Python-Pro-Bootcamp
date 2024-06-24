try:
    file = open('a_file.txt')
except FileNotFoundError:
    print("The file was not found")
    file = open('a_file.txt', 'w')
    file.write("Something")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
