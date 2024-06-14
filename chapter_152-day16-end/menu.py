from menu_item import MenuItem

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("latte", 200, 150, 24, 2.5),
            MenuItem("espresso", 50, 0, 18, 1.5),
            MenuItem("cappuccino", 250, 50, 24, 3.0),
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options.strip("/")

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print(f"Sorry, we don't have a {order_name}.")
        return None
