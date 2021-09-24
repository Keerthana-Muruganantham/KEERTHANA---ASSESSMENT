# Extending a base class

class Vehicle:
    def __init__(self, name, max_speed, mileage ):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def details(self):
        print('Vehicle name: ',self.name)
        print('Vehicle max_speed: ', self.max_speed)
        print('Vehicle mileage: ', self.mileage)

obj = Bus('safari', '200', '240')
obj.details()