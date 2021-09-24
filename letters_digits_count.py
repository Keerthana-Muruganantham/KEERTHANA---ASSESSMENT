def char_count(string):
    digit=0
    letter = 0
    for ch in string:
        if ch.isdigit():
            digit=digit+1
        elif ch.isalpha():
            letter=letter+1
        else:
            continue
    print("LETTERS", letter)
    print("DIGITS", digit)

if __name__ == '__main__':
    string = input("Enter string : ")
    char_count(string)
