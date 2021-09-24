def first_last(a):
    fl = []
    fl.append(a[1])
    fl.append(a[-1])
    return fl
if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    fl = first_last(a)
    print(fl)