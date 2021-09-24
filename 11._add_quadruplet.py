num = int(input("Enter the list length:" ))
a = []
print("Enter the elements")
for i in range(0, num):
    ele = int(input())
    a.append(ele)
print("The list is  ", a)
value = 0
d = []
for i in a:
    value = value+i
for i in a:
    b=a.copy()
    b.remove(i)
    for j in b:
        c = b.copy()
        c.remove(j)
        sum = 0
        for k in c:
            sum = sum + k
        if (sum == value):
            c.sort()
            if c not in d:
                print(c)
                d.append(c)

