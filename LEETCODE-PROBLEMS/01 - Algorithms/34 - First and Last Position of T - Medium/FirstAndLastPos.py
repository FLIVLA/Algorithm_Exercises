"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

"""

class FirstAndLastPos(object):
    
    # Binary search used here - Awesome!
    # Time Complexity: Logarithmic | O(log n)
    def firstAndLast(self, nums, t):
        fst, lst = -1, -1  # indices for positions of first and last instance of t in nums
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == t:
                fst = m
                lst = m
                while fst > 0 and nums[fst - 1] == t:              # Search for fst
                    fst -= 1
                while lst < len(nums) - 1 and nums[lst + 1] == t:  # Search for lst
                    lst += 1
                return [fst, lst]
            elif nums[m] < t:
                l = m + 1
            else:
                r = m - 1
        return [fst, lst]