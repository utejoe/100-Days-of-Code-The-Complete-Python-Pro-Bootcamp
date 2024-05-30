def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

# Getting user inputs
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

# Formatting the name
formatted_name = format_name(first_name, last_name)
print(formatted_name)
