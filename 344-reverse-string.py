"""
need to swap h - o, e - l, and leave l
make left and right pointers
while left < right
    swap left pointer value with right pointer value
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1


solve = Solution()
solve.reverseString(["h", "e", "l", "l", "o"])
print(solve)

































