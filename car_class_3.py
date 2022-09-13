class Car:
    def __init__(self, n, c) -> None:
        self.name = n
        self.color = c

    def start(self):
        print("Start the Engine")


my_car = Car("Porshe", "Charcoal")

print(my_car.color)
print(my_car.name)

my_car.start()

Car.name()
