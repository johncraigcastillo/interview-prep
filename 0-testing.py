"""
Use XOR ^ operator
2 ^ 2 = 0
2 ^ 2 ^ 1 = 1

nums [2, 2, 1]
result = 0
for num in nums:
    result ^= num
return result
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


def main():
    nums = [4, 1, 2, 1, 2]
    solution = Solution()
    print(solution.singleNumber(nums))


if __name__ == "__main__":
    main()

"""
time: O(n)
    just iterating through the entire array of nums
space: O(1)
    no extra space needed
"""
