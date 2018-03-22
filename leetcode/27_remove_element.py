# https://leetcode.com/problems/remove-element/description/
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = 0

        while p < len(nums):
            if nums[p] == val:
                nums.pop(p)
            else:
                p += 1
        return len(nums)
