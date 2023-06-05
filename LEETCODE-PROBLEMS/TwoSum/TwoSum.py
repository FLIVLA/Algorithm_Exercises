# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

# Note:
# goal is to solve it with an O(n) algorithm.

class TwoSum(object):
    
    # This is not a very efficient solution
    # as the algorithm is O(n^2) time complexity
    def twoSum_1(self, nums, t):
        for i in range(len(nums)):
            j = len(nums) - 1
            while j > i:
                if nums[i] + nums[j] == t:
                    return [i, j]
                else: 
                    j -= 1

    #--------------------------------------------------------------
    
    # This approach is optimal for the twoSum problem,
    # as we solve it with O(n), single loop over the input array.
    
    # the for loope iterates over the array of integers
    # and uses enumerate to get both index and number
    # of current iteration.
    # In each iteration c = t - num is calculated
    # and if c exist in the hashtable, we return
    # [hashtable[c], i]. if not, num is added to the hashtable
    # with index i. 
    def twoSum_2(self, nums, t):
        hash_tbl = {} 
        for i, num in enumerate(nums):
            c = t - num 
            if c in hash_tbl:
                return [hash_tbl[c], i]
            hash_tbl[num] = i               # { num: i, ... }
        return []
 
        
#------------------ TEST ------------------

ts = TwoSum()
nums = [2,7,11,15]
t = 9

print(ts.twoSum_1(nums, t))
print(ts.twoSum_2(nums, t))