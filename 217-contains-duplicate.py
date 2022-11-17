class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique = set()
        for num in nums:  # O(n)
            if num in unique:  # O(1) for searching in hash set
                return True
            unique.add(num)  # O(1)
        return False


"""
time complexity:
    O(n) - At most we should iterate through the entire nums array
        So that is O(n).  Checking if num in a hash set is O(1) on average.
space complexity:
    O(n) - We are making a set that could be at most the same size as nums
"""


def main():
    solved = Solution()
    nums = [1, 2, 3, 1]
    # nums = [1, 2, 3, 4]
    solution = solved.containsDuplicate(nums)
    print(solution)


if __name__ == "__main__":
    main()
