def find_three_sum(nums):
    ans = []
    nums.sort()
    # fix i
    for i in range(len(nums)):
        # duplicate num
        if i > 0 and nums[i] == nums[i-1] :
            continue
        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else: 
                ans.append([nums[i], nums[j], nums[k]])
                j += 1

                while nums[j] == nums[j-1] and j<k:
                    j += 1
    return ans

nums = [int(i) for i in input("Enter Your List : ").split()]
if len(nums) < 3 : 
    print("Array Input Length Must More Than 2")
else:
    print(find_three_sum(nums))