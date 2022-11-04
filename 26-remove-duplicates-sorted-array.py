# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
Function must return the resulting length of the list after "removing"
the duplicates

input:  nums = [1,1,2]
output: 2 nums = [1,2,_]   # _ means the value is irrelevant
"""


class Solution:
    """
    nums is sorted in increasing order
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left


nums = [0, 0, 1, 1, 2]
# nums = [0]
solution = Solution()
k = solution.removeDuplicates(nums)
print(f"nums: {nums}")
print(f"k: {k}")

"""
time complexity: O(n)
    right just iterates through the entire array
    left moves k times through the array so it's n + k which is O(n)
space complexity: O(1)
    nums is changed in place
"""
