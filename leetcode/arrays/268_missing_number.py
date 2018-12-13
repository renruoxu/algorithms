class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = {k:True for k in range(len(nums) + 1)}
        for n in nums:
            vals.pop(n)
        return vals.keys()[0]
            
