class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique = set()
        for num in nums:  # O(n)
            if num in unique:  # O(1) for searching in hash set
                return True
            unique.add(num)    # O(1)
        return False


def main():
    solved = Solution()
    nums = [1, 2, 3, 1]
    # nums = [1, 2, 3, 4]
    solution = solved.containsDuplicate(nums)
    print(solution)


if __name__ == "__main__":
    main()
