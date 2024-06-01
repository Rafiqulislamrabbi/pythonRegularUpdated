class Vehicle:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def get_description(self):
        return f"{self.year} {self.make} {self.model} (${self.price})"


class Car(Vehicle):
    def __init__(self, make, model, year, price, num_doors):
        super().__init__(make, model, year, price)
        self.num_doors = num_doors

    def get_description(self):
        return f"{super().get_description()}, {self.num_doors} doors"


class Truck(Vehicle):
    def __init__(self, make, model, year, price, payload_capacity):
        super().__init__(make, model, year, price)
        self.payload_capacity = payload_capacity

    def get_description(self):
        return f"{super().get_description()}, Payload: {self.payload_capacity} lbs"


class Van(Vehicle):
    def __init__(self, make, model, year, price, seating_capacity):
        super().__init__(make, model, year, price)
        self.seating_capacity = seating_capacity

    def get_description(self):
        return f"{super().get_description()}, Seating Capacity: {self.seating_capacity}"


# Example usage:
car = Car("Toyota", "Camry", 2022, 25000, 4)
truck = Truck("Ford", "F-150", 2021, 35000, 2000)
van = Van("Honda", "Odyssey", 2020, 30000, 7)

print(car.get_description())
print(truck.get_description())
print(van.get_description())
