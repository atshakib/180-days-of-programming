def twoSum(nums: list, target: int) -> list:
    result = []
    for num in nums:
        for i in range(len(nums)):
            if nums[i] + num == target:
                result.append(i)
                result.append(nums.index(num))
                return result

print(twoSum([2,7,11,15] , 9))
