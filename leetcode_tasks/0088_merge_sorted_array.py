class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2[:]
            return
        if n == 0: return
        
        p1, p2, t = m-1, n-1, m+n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[t] = nums1[p1]
                t, p1 = t - 1, p1 - 1
            else:
                nums1[t] = nums2[p2]
                t, p2 = t - 1, p2 - 1
        
        if p2 >= 0:
            nums1[:p2+1] = nums2[:p2+1]