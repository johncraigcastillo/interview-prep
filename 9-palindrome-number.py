class Solution:
    def isPalindromeByStringConversion(self, x: int) -> bool:
        """Given an integer, return true if x is a palindrome"""
        numString = str(x)
        left, right = 0, len(numString) - 1
        while left < right:
            if numString[left] != numString[right]:
                return False
            left, right = left + 1, right - 1
        return True

    def isPalindromeBetter(self, x: int) -> bool:
        """This goes through the whole number"""
        print(f"Original x: {x}")
        inputNum = x
        revNum = 0
        while x > 0:
            revNum = revNum * 10 + x % 10
            print(f"revNum: {revNum}")
            x = x // 10
        return revNum == inputNum

    def isPalindromeBest(self, x: int) -> bool:
        """Goes through half the number"""
        # if x is negative, or x is positive and first digit is 0
        if x < 0 or x > 0 and not x % 10:
            return False
        revNum = 0
        while x > revNum:
            revNum = revNum * 10 + x % 10
            print(f"revNum: {revNum}")
            x = x // 10
        print(f"x: {x} revNum: {revNum}")
        return revNum == x or x == revNum // 10


solution = Solution()
# print(solution.isPalindromeByStringConversion(323))
# print(solution.isPalindromeBetter(32123))
print(solution.isPalindromeBest(32123))
