class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pos = {}
        for i,n in enumerate(nums):
            if n in pos:
                if i - pos[n] <= k:
                    return True
                else:
                    pos[n] = i
            else:
                pos[n] = i
        return False