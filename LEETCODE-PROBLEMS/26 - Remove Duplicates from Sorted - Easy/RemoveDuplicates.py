class RemoveDuplicates(object):
    
    # Clumsy approach
    def removeduplicates(self, nums):
        s = set()
        res = []
        for n in nums:
            s.add(n)
        for n in s:
            res.append(n)
        return res
    
    # Also known as runner technique
    def removeDuplicates_twoPointer(self, nums):
        i, j = 0, 0                 # initialize pointers i and j
        while j < len(nums):        
            if nums[j] != nums[i]:  # check if i and j of nums match
                i += 1              # move i right
                nums[i] = nums[j]   # swap i and j of nums
            j += 1                  # move j right
        return nums[:i + 1]         # return sliced to last unique element
        # return len(nums[:i + 1])  # return this for the number of unique elements
        

rd = RemoveDuplicates()
print(rd.removeDuplicates_twoPointer([1,1,2,3]))