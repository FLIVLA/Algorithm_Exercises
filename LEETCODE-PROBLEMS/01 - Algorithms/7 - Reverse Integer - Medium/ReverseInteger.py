#
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit 
# integer range [-231, 231 - 1], then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# 
# Example 1:
# - Input: x = 123
# - Output: 321
#

import math

class ReverseInt(object):
    
    # Time Complexity: Linear | O(n) where n is the number of digits in x
    def reverseInt(self, x):
        if x == 0: return x
        else:
            revStr = str(abs(x))[::-1] # reverse by slicing, instead of traditional loop
            if x < 0: 
                revStr = "-" + revStr
            if int(revStr) >= -math.pow(2, 31) and int(revStr) <= math.pow(2, 31) - 1:
                return int(revStr)
            else: return 0
    
    # Avoid conversion from int to string, and use mathematical
    # operators to reverse digits instead.
    # this will speed up the process significantly! 
    def reverseInt_turboMode(self, x):
        s = -1 if x < 0 else 1
        y = abs(x)  # absolute value of x
        r = 0       # initialize rev int
        while y > 0:
            r = r * 10 + y % 10  # accumulate rev digits
            y = y // 10          # remove last digit
        
        # check for r within valid range of 32-bit int
        if r > 2**31 - 1 or r < -2**31: 
            return 0
        return r * s # return reversed  