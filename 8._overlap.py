def merge(arr, n, newPair):
    stk = []
    stk.append(arr[0])
    top = stk[len(stk) - 1]
    if (newPair[0] < top[1]):
        stk.pop()
        top[0] = min(top[0], newPair[0])
        top[1] = max(top[1], newPair[1])
        stk.append(top)
    else:
        stk.append(newPair)
    for i in range(1, n):
        top = stk[len(stk) - 1]
        if (arr[i][0] < top[1]):
            stk.pop()
            top[0] = min(top[0], arr[i][0])
            top[1] = max(top[1], arr[i][1])
            stk.append(top)
        else:
            stk.append(arr[i])
    Intervals = []
    while (len(stk) > 0):
        ele = stk[len(stk) - 1]
        stk.pop()
        Intervals.append(ele)
    while (len(Intervals) > 0):
        ele = Intervals[len(Intervals) - 1]
        Intervals.pop()
        print(ele[0], end=", ")
        print(ele[1])


arr = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newPair = [4, 9]
n = len(arr)
merge(arr, n, newPair)
