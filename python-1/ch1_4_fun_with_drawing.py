num = input("*** Fun with Drawing ***\nEnter input : ")
size = ((int(num) - 1)*4) + 1

# row
for i in range(size): 
    # column
    for j in range(size):
        top = (i%2 == 0) and (i <= j < (size - i))
        bottom = (i%2 == 0) and ((size - i - 1) <= j <= i)
        left = (j%2 == 0) and (j <= i < (size - j))
        right = (j%2 == 0) and ((size - j - 1) <= i <= j)
        if top or bottom or left or right: print("#", end="")
        else: print(".", end="")
    print("")