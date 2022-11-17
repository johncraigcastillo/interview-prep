"""
create empty set
for num in nums:
    if num in set:
        return True
    add num to set
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False


def main():
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.containsDuplicate(nums))


if __name__ == "__main__":
    main()


"""
time complexity: O(n)
    inserting into set and checking if in a hash set is constant
    interating through nums is n
space complexity: O(n)
    we must at most create a set of size n
"""
