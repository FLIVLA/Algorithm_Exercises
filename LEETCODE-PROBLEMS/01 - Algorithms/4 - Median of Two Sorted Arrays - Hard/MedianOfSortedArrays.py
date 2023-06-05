# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#--------------------------------------------------------
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#--------------------------------------------------------

class MedianOfSortedArrays(object):
    def medianOfSorted(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        