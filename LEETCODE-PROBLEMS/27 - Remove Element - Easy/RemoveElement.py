class RemoveElement(object):
    
    # Time Complexity: Linear | O(n)
    def removeElement_twoPointer(self, nums, val):
        i, j = 0, 0                 # Initialize pointers
        while j < len(nums):
            if nums[j] == val:
                j += 1              # move right pointer only
            else:
                nums[i] = nums[j]   # swap elements
                i += 1              # move left pointer
                j += 1              # move right pointer
        return nums[:i]             # Return sliced
    
    # filter method, with lambda expression
    def removeElement_filter(self, nums, val):
        return list(filter(lambda x: x != val, nums))


re = RemoveElement()
nums = [1,1,2,3]
val = 3
print(re.removeElement_twoPointer(nums, val))
print(re.removeElement_filter(nums, val))