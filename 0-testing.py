"""
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Explanation: Your function should return k = 5, with the first five elements
of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are
underscores).
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # if the array is empty
        if len(nums) < 1:
            return 0

        # left pointer will start at index 1
        left = 1

        # move right pointer from index 1 to last index
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left


def main():
    solved = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # nums = []
    solution = solved.removeDuplicates(nums)
    print(solution)


if __name__ == "__main__":
    main()
