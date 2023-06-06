# You are given a large integer represented as an 
# integer array digits, where each digits[i] is the 
# ith digit of the integer. The digits are ordered from most 
# significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the 
# resulting array of digits.

class PlusOne(object):
    
    # Time complexity of this solution is O(n)
    def plusOne(self, digits):
        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if i > 0:
                if digits[i] == 10:
                    digits[i] = 0
                    digits[i - 1] += 1
                else: break             # BREAK! decreases runtime significantly
            else:
                if digits[i] == 10:
                    digits[i] = 1
                    digits.append(0)
        return digits
    
    # inspired by leetcode sln, though the implementation
    # is simpler, it should not be used for very large numbers
    def plusOne_compact(self, digits):
        res = []
        num = int(''.join(str(e) for e in digits)) + 1
        for d in str(num):
            res.append(int(d))
        return res
        


po = PlusOne()
digs = [9,9,9,9]
print(po.plusOne(digs))