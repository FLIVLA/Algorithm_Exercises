class ThreeSum(object):
    # quick sort implementation
    def sort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            p = nums[0]
            l = [x for x in nums[1:] if x <= p]
            r = [x for x in nums[1:] if x > p]
            return self.sort(l) + [p] + self.sort(r)
    
    def threeSum(self, nums):
        triplets = []
        nums = self.sort(nums)
        if len(nums) == 3 and sum(nums) == 0:
            triplets.append(nums)
            return triplets
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif 0 < t:
                    r -= 1
                else:
                    l += 1
        return triplets

nums = [-1,0,1,2,3,4]
print(nums[1:])
ts = ThreeSum()
print(ts.threeSum(nums))
