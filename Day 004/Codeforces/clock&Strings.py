class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []

# Taking input for nums as a string
nums_str = input()

# Remove brackets and spaces, then split the string by commas
nums = list(map(int, nums_str.strip('[]').replace(' ', '').split(',')))

# Taking input for target
target = int(input())

# Create an instance of the Solution class
solution = Solution()

# Call the twoSum method and print the result
print(solution.twoSum(nums, target))
