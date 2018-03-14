# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

#### brute force
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        array = nums1 + nums2
        array = sorted(array)
        mid = len(array) / 2
        if len(array) % 2 == 0:
            return (array[mid] + array[mid-1]) / 2.
        else:
            return array[mid]