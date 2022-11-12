class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead
        k = 3
        imput:  [1, 2, 3, 4, 5, 6, 7]
        output: [5, 6, 7, 1, 2, 3, 4]
        """
        k = k % len(nums)
        if len(nums) < 2:
            return

        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        left, right = 0, k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        left, right = k, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        print(nums)


def main():
    solve = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solve.rotate(nums, k)


if __name__ == "__main__":
    main()
