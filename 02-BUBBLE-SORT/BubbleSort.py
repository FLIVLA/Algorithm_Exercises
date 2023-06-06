class BubbleSort(object):
    
    # Time complexity: Quadratic | O(n^2)
    def sort(self, nums):
        n = len(nums) - 1
        for i in range(0, n):
            for j in range(0, n - i):
                if nums[j] > nums[j + 1]: # swap elements
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
        return nums

    # sorts and counts iterations
    def sort_withStats(self, nums):
        comp, swap = 0, 0
        n = len(nums) - 1
        for i in range(0, n):
            for j in range(0, n - i):
                comp += 1                 # count comparisons
                if nums[j] > nums[j + 1]: # swap elements
                    swap += 1             # count swaps 
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp 
        print("Comparisons: ", comp)
        print("Swaps: ", swap)      
        return nums
    
    # test for larger inputs
    def sort_file_withStats(self, nums_path):
        with open(nums_path, 'r') as file:
            nums = [int(num) for num in file.read().split(", ")]  
        comp, swap = 0, 0
        n = len(nums) - 1
        for i in range(0, n):
            for j in range(0, n - i):
                comp += 1                 # count comparisons
                if nums[j] > nums[j + 1]: # swap elements
                    swap += 1             # count swaps 
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp 
        print("Comparisons: ", comp)
        print("Swaps: ", swap)      
        return nums
    

# ------------------- TEST -------------------

bs = BubbleSort()
bs.sort_file_withStats('C:/Users/Frederik/source/vs_code/KSALDAS/BUBBLE-SORT/inputs/5k_input.txt')
bs.sort_file_withStats('C:/Users/Frederik/source/vs_code/KSALDAS/BUBBLE-SORT/inputs/10k_input.txt')