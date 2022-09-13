class Car:

    def __init__(self, name, manufacturer, color, year, cc) -> None:
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.cc = cc

    def start(self):
        print(f"{self.name} is starting!")

    def brake(self):
        print(f"{self.name} is braking!")

    def drive(self):
        print(f"{self.name} is driving!")

    def turn(self):
        print(f"{self.turn} is turning!")

    def gear_shifting(self):
        print(f"{self.name} is shifting gear!")


my_tesla = Car("modelX", "tesla", "black", 2021, "ev")


print(my_tesla.name)

my_tesla.gear_shifting()

print(my_tesla.year)
