class QuickSort(object):
    def sort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            p = nums[0]
            l = [x for x in nums[1:] if x <= p]
            r = [x for x in nums[1:] if x > p]
            return self.sort(l) + [p] + self.sort(r)