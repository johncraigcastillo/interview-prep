"""
issues: forgot to modulus k against len(nums)
3 % 3 = 0 because the remainder of 3 / 3 is 0
10 % 3 = 1 because the remainder of 10/3 is 1
3 % 10 = 3 because the remainder of 3 / 10 is 3
    10 goes into 3 0 times. so 3 remains
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        # reverse whole thing
        reverse_section(nums, 0, len(nums) - 1)
        # reverse from 0 to k-1
        reverse_section(nums, 0, k - 1)
        # reverse from k to len(nums)-1
        reverse_section(nums, k, len(nums) - 1)
        print(nums)


def reverse_section(nums: list[int], left: int, right: int):
    """
    while left < right:
       nums[left], nums[right] = nums[right], nums[left]
       left++
       right--
    """
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def main():
    solution = Solution()
    nums = [1, 2, 3, 4]
    k = 1
    """
    1, 2, 3, 4
    k = 1
    out: 4, 1, 2, 3
    1. reverse
        4, 3, 2, 1
    2. reverse from index 0, k-1
    3. reverse from index k, len(nums) - 1
    """
    solution.rotate(nums, k)


if __name__ == "__main__":
    main()
