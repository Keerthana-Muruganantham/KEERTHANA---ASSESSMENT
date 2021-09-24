num=int(input("Enter the list length :  "))
a = []
b = []
c = []
print("Enter the elements")
for i in range(0, num):
    element = int(input())
    a.append(element)
print("The list is  ", a)
for i in range(0, num) :
    b = a.copy()
    b[i] = 1
    res = 1
    for i in range(0, num):
        res = res*b[i]
    c.append(res)
print (c)