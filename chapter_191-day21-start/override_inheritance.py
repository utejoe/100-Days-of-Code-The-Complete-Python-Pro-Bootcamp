class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.location = "water"

    def breathe(self):
        super().breathe()  # Call the breathe method of the superclass
        print("Doing this underwater")


nemo = Fish()
nemo.breathe()

