class RomanToInt(object): 
    
    # Define char map for roman numerals
    def __init__(self):
        self.charMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    def convert(self, s):
        r = 0
        for i in range(len(s) - 1, -1, -1):
            if i + 1 < len(s) and self.charMap.get(s[i]) < self.charMap.get(s[i + 1]):
                if s[i] == 'I' and s[i + 1] != 'I':
                    r -= 1
                else: r -= self.charMap.get(s[i])
            else: r += self.charMap.get(s[i])
        return r

# TEST THE CONVERSION
ri = RomanToInt()
print(ri.convert('CM'))