class Solution(object):   
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1, count2 = {}, {}
        for n in nums1:
            count1[n] = count1.get(n, 0) + 1
        for n in nums2:
            count2[n] = count2.get(n, 0) + 1
        
        common = []
        for k, v in count1.iteritems():
            if k in count2:
                common += [k] * min(v, count2[k])
        return common
