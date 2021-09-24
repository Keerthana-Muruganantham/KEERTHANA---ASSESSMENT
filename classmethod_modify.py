# Call the class method to modify the member variable

class person:
    def __init__(self, a='Priya', b='Female'):
        self.name = a
        self.gender = b
    def show_info(self):
        print('Name: ', self.name)
        print('Gender: ', self.gender)
p1 = person('Raj', 'Male')
p1.show_info()