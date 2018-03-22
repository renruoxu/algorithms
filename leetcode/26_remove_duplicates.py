# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) >1:

            curr_p = 1

            while curr_p < len(nums):
                if nums[curr_p] == nums[curr_p - 1]:
                    nums.pop(curr_p)
                else:
                    curr_p += 1
