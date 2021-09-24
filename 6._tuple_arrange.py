from operator import itemgetter
num = int(input("Enter the Records:"))
tuple = ()
for i in range(0, num):
    temp = []
    name = input('Enter the name:')
    temp.append(name)
    age = input('Enter the age:')
    temp.append(age)
    height = input('Enter the height:')
    temp.append(height)
    tuple = (tuple ) + (temp,)
print(tuple)
tup=sorted(tuple, key = itemgetter(0, 1, 2))
print(tup)