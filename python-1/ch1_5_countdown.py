lst = input("*** Fun with countdown ***\nEnter List : ")
nums = [int(num) for num in lst.split()]
i = len(nums) - 1
countdown = [0, []]

while i >= 0:
    if (nums[i] == 1):
       ans = [1]
       i-=1
       while i >= 0 and nums[i] == nums[i + 1] + 1:
            ans.insert(0, nums[i])
            i-=1
       countdown[0] += 1
       countdown[1].insert(0, ans)
    else:
        i-=1
print(countdown)