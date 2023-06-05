class ContainsDuplicate(object):
    def check(self, nums):
        ex = set() # create empty set
        for x in nums:
            if x in ex:
                return True
            else:
                ex.add(x) # add num at position x in nums
        return False
    
    # create set from nums, as sets contains only unique items, 
    # the len will be smaller if nums contains dups.
    # The Runtime is a lot shorter for this method than the method above
    def checkHyperSpeed(self, nums):
        ex = set(nums) 
        if len(ex) == len(nums):
            return False
        else: return True
        