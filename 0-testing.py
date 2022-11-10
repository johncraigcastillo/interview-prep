class Solution:
    """
    left = 0
    for i range(1, len(nums)):
        right = i
        if nums[left] != nums[right]:
                nums[left + 1] = numsRight
                left += 1
              l        r
    [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]

    """

    def removeDuplicates(self, nums: list[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right - 1] != nums[right]:
                nums[left] = nums[right]
                left += 1
        return left


"""
time complexity: O(n)
    iterating through entire list
space: O(1)
    everything is done in place
"""

solve = Solution()
nums = [1]
k = solve.removeDuplicates(nums)
print(k)
