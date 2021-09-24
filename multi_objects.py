# Create multiple objects for this class with different values passed to the constructor.

class person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def show_info(self):
        print('Name: ', self.name)
        print('Gender: ', self.gender)

p1 = person('Raj', 'Male')
p1.show_info()

p2 = person('Vani', 'Female')
p2.show_info()

p3 = person('Arun', 'Male')
p3.show_info()