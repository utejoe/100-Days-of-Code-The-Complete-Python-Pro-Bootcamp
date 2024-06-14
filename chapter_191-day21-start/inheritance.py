class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()  # Call the superclass initializer
        self.location = "water"

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()  # Output: Moving in water
nemo.breathe()  # Output: Inhale, exhale
print(nemo.num_eyes)  # Output: 2
