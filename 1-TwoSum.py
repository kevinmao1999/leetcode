# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution:
    # solution1 loops over each element in the list and does a second nested loop within to check if values add up
    # O(n^2) time complexity caused by the nested loop
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # solution2 loops over each element in the list once and maps them to a dictionary with the index as value
    # runs a second separate loop that checks for the needed value from the dict
    # first loop runs in O(n) time to add to a dict
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            mydict[nums[i]] = i
        for i in range(len(nums)):
            val = target - nums[i]
            if val in mydict and mydict[val] != i:
                return [i, mydict[val]]
        return []

        