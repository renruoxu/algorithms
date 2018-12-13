class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        subseq_dict = {float('-inf'): 0}

        for n in nums:
            for k, v in subseq_dict.items():
                if n > k:
                    subseq_dict[n] = max(subseq_dict[k] + 1, subseq_dict.get(n, 0))
                    if subseq_dict[n] > max_length:
                        max_length = subseq_dict[n]
        return max_length