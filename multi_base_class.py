#  Create a base class Vehicle. Extend the class and create Car and Bus. create objects for these classes

class Vehicle:
    def __init__(self, name, max_speed, mileage ):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        def show_info():
            print()

class Bus(Vehicle):
    def details(self):
        print('Vehicle name: ',self.name)
        print('Vehicle max_speed: ', self.max_speed)
        print('Vehicle mileage: ', self.mileage)

obj = Bus('safari', '200', '240')
obj.details()

class Car(Vehicle):
    def details(self):
        print('Vehicle name: ',self.name)
        print('Vehicle max_speed: ', self.max_speed)
        print('Vehicle mileage: ', self.mileage)

obj = Car('mahindra', '180', '260')
obj.details()

