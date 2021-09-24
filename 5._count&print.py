str = input("Enter the string: ")
temp = ' '
for char in str:
    if char not in temp:
        print(char, str.count(char))
        temp = temp + char
