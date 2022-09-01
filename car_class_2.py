class Car:
    name = ""
    color = ""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start(self):
        print("Starting the Engine")


my_car = Car("Porshe", "Charcoal")

print(my_car.name)
print(my_car.color)

my_car.start()
