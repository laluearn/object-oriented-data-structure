def bubble(lst, index = 0, sorts = True):
    if sorts and index == len(lst) - 1:
        return lst
    if index == len(lst)-1:
        sorts = True
        index = 0
    if lst[index] > lst[index + 1]:
        sorts = False
        lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return bubble(lst, index + 1, sorts)

inputs = [int(num) for num in input("Enter Input : ").split()]
print(bubble(inputs))