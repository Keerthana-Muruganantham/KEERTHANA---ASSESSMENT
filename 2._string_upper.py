class string:
    def getString(self):
        name = input("Enter your Name: ")
        return name
    def printString(self, name):
        print(name.upper())
        return
obj = string()
name = obj.getString()
obj.printString(name)
