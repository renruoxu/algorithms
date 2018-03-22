# https://leetcode.com/problems/search-insert-position/description/
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        start = 0
        end = len(nums) - 1
        mid = (start + end) / 2
        while (start < end):
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[start] == target:
                    return start
                start = mid + 1
                mid = (start + end) / 2
            else:
                end = mid - 1
                mid = (start + end) / 2

        if nums[end] < target:
            return end + 1
        else:
            return end
