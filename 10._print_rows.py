def printRows(num):
    for row in range(1, num + 1):
        C = 1
        for i in range(1, row + 1):
            print(C, end=" ")
            C = int((C * (row - i)) / i)
        print("")
num = 5
printRows(num)