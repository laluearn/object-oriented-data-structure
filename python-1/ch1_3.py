print(" *** Summation of each digit ***")
num = input("Enter a positive number : ")
sum = 0
for i in range(len(num)) : sum += int(num[i])
print("Summation of each digit = ", sum)