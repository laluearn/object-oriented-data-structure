def staircase(i, n):
    if i == n:
        return
    if n > 0:
        print("_"*(n-i-1) + "#"*(i+1))
        staircase(i+1, n)
    elif n < 0:
        staircase(i-1, n)
        j, k = abs(i), abs(n)
        print("_"*(k-j-1) + "#"*(j+1))

staircase(0, int(input("Enter Input : ")))