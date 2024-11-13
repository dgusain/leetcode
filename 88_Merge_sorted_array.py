'''
88 Merge sorted array
nums1, nums2, m, n: merge them in-place sorting, 
'''
class Solution:
    def merge(self, nums1:list[int], m:int, nums2:list[int], n:int):
        p1 = m-1
        p2 = n-1
        p = m+n-1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        nums1[:p2+1] = nums2[:p2+1]
         