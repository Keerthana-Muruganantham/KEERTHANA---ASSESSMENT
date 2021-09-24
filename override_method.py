# Override a method

class Vehicle:
    def __init__(self, name, max_speed, mileage ):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def show_info(self):
        print('Vehicle name: ', self.name)
        print('Vehicle max_speed: ', self.max_speed)
        print('Vehicle mileage: ', self.mileage)

class Bus(Vehicle):
    def show_info(self):
        print('Vehicle name: ',self.name)
        print('Vehicle max_speed: ', self.max_speed)
        print('Vehicle mileage: ', self.mileage)

obj1 = Vehicle('mahindra', '180', '250')
obj1.show_info()

obj2 = Bus('safari', '200', '240')
obj2.show_info()
