# https://leetcode.com/problems/maximum-subarray/description/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None

        minSum = 0
        maxSum = nums[0]
        curr_sum = 0

        for n in nums:
            curr_sum += n

            if curr_sum - minSum > maxSum:
                maxSum = curr_sum - minSum
            if curr_sum < minSum:
                minSum = curr_sum
        return maxSum
