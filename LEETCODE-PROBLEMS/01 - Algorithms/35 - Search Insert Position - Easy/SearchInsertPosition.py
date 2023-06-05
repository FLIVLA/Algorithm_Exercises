"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the 
index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

------------------------------------------------------------------
 
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

-------------------------------------------------------------------
Constraints:
    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    nums contains distinct values sorted in ascending order.
    -10^4 <= target <= 10^4

"""

class SearchInsertPos(object):
    
    # Binary search approach.
    # Time Complexity: Logarithmic | O(log n)
    def searchInserPos(self, nums, t):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l + 1) // 2  # update middle index for each iteration
            if nums[m] < t:
                l = m + 1
            elif nums[m] > t:
                r = m - 1
            else: return m 
        return l
            
            
#------------------ TEST ------------------
nums = [1,3,5,6]
t = 6
sip = SearchInsertPos()
print(sip.searchInserPos(nums, t))     
        