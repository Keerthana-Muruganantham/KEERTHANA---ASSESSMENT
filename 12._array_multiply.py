n = int(input("Enter the number of elements : "))
a = []
print("Enter the elements")
for i in range(0, n):
    element = int(input())
    a.append(element)
print(" The list is  ", a)
a.sort(reverse=True)
print("Highest product in the list is", a[0]*a[1]*a[2])