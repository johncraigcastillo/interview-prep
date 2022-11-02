class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash = set()
        for num in nums:
            if num in hash:
                return True
            hash.add(num)
        return False

    def containsDuplicateAlt(self, nums: list[int]) -> bool:
        return not len(nums) == len(set(nums))


solution1 = Solution()
print(solution1.containsDuplicate([1, 2, 3, 4]))

solution2 = Solution()
print(solution2.containsDuplicateAlt([1, 2, 3, 4]))
