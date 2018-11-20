class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < k:
            last = nums.pop()
            nums.insert(0, last)
            i += 1