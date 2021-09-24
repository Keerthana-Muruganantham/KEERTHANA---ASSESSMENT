def form_dict():
    num_dict = {}
    for i in range(1, 21):
        temp  = i
        num_dict[i] = temp**2

    return num_dict
if __name__ == '__main__':
    num_dict = form_dict()
    print(num_dict)