fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Error pie")
    else:
        print(f"{fruit} pie")

# Test the function
make_pie(0)  # Should print "Apple pie"
make_pie(1)  # Should print "Pear pie"
make_pie(2)  # Should print "Orange pie"
make_pie(4)  # Should print "Fruit pie"
