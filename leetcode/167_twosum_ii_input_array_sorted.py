class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement = {}
        for i,n in enumerate(numbers):
            if n in complement:
                return [complement[n], i + 1]
            else:
                c = target - n
                if c >= n:
                    complement[c] = i + 1