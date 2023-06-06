class SelectionSort(object):
    
    # Time Complexity: Quadratic | O(n^2) where n is the length of nums
    def sort(self, nums):
        n = len(nums)
        for i in range(len(nums)):
            min = i
            for j in range(i + 1, n):
                if nums[j] < nums[min]:
                    min = j
            nums[i], nums[min] = nums[min], nums[i] 
        return nums

nums = [5,2,4,1,7,9,35,32,77]
ss = SelectionSort()
print(ss.sort(nums))