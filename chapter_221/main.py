# Reading from a file
with open("c:/Users/User/Desktop/software_work/projects/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp/chapter_221/my_file.txt") as file:
    contents = file.read()
    print(contents)



# Writing to a file
with open("c:/Users/User/Desktop/software_work/projects/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp/chapter_221/new_file.txt", mode="w") as file:
    file.write("Hello, my name is uyi.")




# Appending to a file
with open("c:/Users/User/Desktop/software_work/projects/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp/chapter_221/my_file.txt", mode="a") as file:
    file.write("\nNew line of text.")
