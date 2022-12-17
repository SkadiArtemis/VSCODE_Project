class Solution:
    def intersect(self, nums1, nums2):
        res = []
        for n in nums1:
            if n in nums2:
                res.append(n)
                nums2.remove(n)
        return res