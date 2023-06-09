"""
Given an integer array nums, rotate the array to the right by k steps, 
where k is non-negative.

"""

# Time Complexity: Linear | O(k * n)
class ArrayRotator(object):
    def rotate(self, nums, k):
        i = 0                                        # step count of k
        while i < k:                                 # iterate until i reaches k iterations
            t = nums[-1]                             # store last element
            for j in range(len(nums) - 1, 0, -1):    # loop r -> l
                nums[j] = nums[j - 1]                # swap nums[j] with element at j-1
            nums[0] = t                              # move last to first
            i += 1                                   # increment step count (k)
        return nums                                  # return rotated result

    # Two pointer approach, moving inwards
    def rotate_speedy(self, nums, k):
        n = len(nums)
        kn = k % n
        
        a0, b0 = 0, n - 1
        while a0 < b0:
            nums[a0], nums[b0] = nums[b0], nums[a0]
            a0 += 1
            b0 -= 1
        
        a1, b1 = 0, kn - 1
        while a1 < b1:
            nums[a1], nums[b1] = nums[b1], nums[a1]
            a1 += 1
            b1 -= 1        
        
        a2, b2 = kn, n - 1
        while a2 < b2:
            nums[a2], nums[b2] = nums[b2], nums[a2]
            a2 += 1
            b2 -= 1
        return nums
        

#------------ TEST ------------

nums = [1,2,3,4,5,6,7]
k = 3
#Output: [5,6,7,1,2,3,4]

ar = ArrayRotator()
print(ar.rotate_speedy(nums, k))