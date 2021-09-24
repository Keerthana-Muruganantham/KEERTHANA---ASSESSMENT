import re
def pass_valid(password):
    if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[$@#])[\w\d$@#]{6,12}$", password):
        print ("valid password")
    else:
        print ("invalid password")

if __name__ == '__main__':
    password = input("Enter password: ")
    pass_valid(password)