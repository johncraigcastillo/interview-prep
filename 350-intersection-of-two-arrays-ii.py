"""
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

sort nums1
sort nums2
nums1 = [1, 1, 2, 2]
nums2 = [2, 2]

result = []
i, j, = 0, 0  #use pointers for nums1, and nums2

while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
        add nums1[i] to result
    if nums1[i] < nums2[j]:
        i++
    if nums1[i] > nums2[j]:
        j++
return result
"""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        nums1.sort()  # O(nlogn)
        nums2.sort()  # O(mlogm)
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):  # O(n + m)
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result


def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    solution = Solution()
    print(solution.intersect(nums1, nums2))


if __name__ == "__main__":
    main()

"""
time: O(nlogn + mlogm)
    sorting n takes nlogn
    sorting m takes mlogm
    iterating through n and m takes n + m
        this part simplifies out
space: O(n + m)
    worst case result is filled completely with the values in m and n
"""
