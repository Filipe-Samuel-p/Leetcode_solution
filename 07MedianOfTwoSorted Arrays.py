class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.extend(nums2)
        nums1.sort()
        le = len(nums1)
        if le % 2 == 0:
            median = (nums1[le//2] + (nums1[le//2 -1]))/ 2
        else:
            median = nums1[le//2] 
        return median