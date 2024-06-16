class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make', 'Unknown')
        self.model = kwargs.get('model', 'Unknown')
        self.color = kwargs.get('color', 'Unknown')
        self.seats = kwargs.get('seats', 4)

# Testing the Car class
my_car = Car(make='Nissan', model='GT-R', color='Red')
print(f"Make: {my_car.make}, Model: {my_car.model}, Color: {my_car.color}, Seats: {my_car.seats}")
