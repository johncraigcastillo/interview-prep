class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for n in nums:
            result = n ^ result
        return result


def main():
    solution = Solution()
    nums = [0, 1, 1, 2, 3, 3, 2, 0, 4]
    result = solution.singleNumber(nums)
    print(result)


if __name__ == "__main__":
    main()
