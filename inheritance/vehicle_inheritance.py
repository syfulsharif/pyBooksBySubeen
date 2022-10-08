class Vehicle:
    """Base class for all vehicles"""

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print(f"Driving ! {self.manufacturer} {self.name}")

    def turn(self, direction):
        print(f"Turning {self.name} to {direction} ")

    def brake(self):
        print(f"{self.name} is stopping!")


if __name__ == "__main__":
    v1 = Vehicle("Fusion 110 Ex", "Walton", "Black")
    v2 = Vehicle("Softail Delux", "Harley Davidson", "Blue")
    v3 = Vehicle("Mustang 5.0 GT Copue", "Ford", "Red")

# v1.drive()
# v3.brake()


class Car(Vehicle):
    """Car Class"""

    def change_gear(self, gear_name):
        """Method for changing gear"""
        print(f"{self.name} is changing gear to {gear_name}")


axio = Car("Axio", "Toytoa", "Grey")


axio.change_gear(4)
axio.brake()
axio.turn("left")
