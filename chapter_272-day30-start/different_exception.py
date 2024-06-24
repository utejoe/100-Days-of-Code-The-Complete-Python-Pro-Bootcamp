try:
    file = open('a_file.txt')
    a_dict = {"key": "value"}
    print(a_dict["non_existent_key"])
except FileNotFoundError:
    print("The file was not found")
    file = open('a_file.txt', 'w')
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
