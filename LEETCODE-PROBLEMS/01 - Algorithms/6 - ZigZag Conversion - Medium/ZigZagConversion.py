# The string "PAYPALISHIRING" is written in a zigzag pattern on 
# a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
#
# Example 1:
# - Input: s = "PAYPALISHIRING", numRows = 3
# - Output: "PAHNAPLSIIGYIR"

class ZigZagConversion(object):
    
    # Initial Attempt
    def zigZag_Convert(self, s, n):
        if n >= len(s): return s
        else:
            rows = ['' for _ in range(n)]    # create n empty rows 
            index, step = 0, 1
            for char in s:
                rows[index] += char
                if index == 0:
                    step = 1
                elif index == n - 1:
                    step = -1
                index += step
        return ''.join(rows)
            

zz = ZigZagConversion()
inp = "PAYPALISHIRING"
print(zz.zigZag_Convert(inp, 3))