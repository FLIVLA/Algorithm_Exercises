
class BinarySearch(object):
    
    def search_PosOf_t(self, nums, t):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l + 1) // 2
            if nums[m] < t:
                l = m + 1
            elif nums[m] > t:
                r = m - 1
            else: return m
        return l