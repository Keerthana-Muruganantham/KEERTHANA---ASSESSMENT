def dec_to_bin(n):
    if(n>1):
        dec_to_bin(n//2)
    print(n%2, end='')

n = int(input("Enter the value to convert it into binary: "))
dec_to_bin(n)
