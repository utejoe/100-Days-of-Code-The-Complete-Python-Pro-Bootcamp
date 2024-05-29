nested_dict = {
    "person1": {
        "name": "Alice",
        "age": 30
    },
    "person2": {
        "name": "Bob",
        "age": 25
    }
}

# Accessing elements
print(nested_dict["person1"])        # Output: {'name': 'Alice', 'age': 30}
print(nested_dict["person1"]["name"]) # Output: Alice
