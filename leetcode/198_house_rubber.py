class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        maxmoney = [0] * len(nums)
        maxmoney[0] = nums[0]
        maxmoney[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            maxmoney[i] = max(maxmoney[i-2] + nums[i], maxmoney[i-1])
        return max(maxmoney)
        
        
