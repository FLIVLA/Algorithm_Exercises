class LongestCommonPrefix(object):
    
    # this was made by misunderstanding the
    # initial problem, though it could probably be useful somehow.
    # It finds longest common substring in a list of strings.
    # Might not be very efficient!
    # Time Complexity: Quadratic | O(n * m)
    def longestCommonSubStringOfTwoElms(self, strs):
        prefix = ""
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                p = ""
                n = 0
                m = len(strs[i]) if len(strs[j]) >= len(strs[i]) else len(strs[j])  # sneaky conditional declaration ;)
                while n < m:
                    if strs[i][n] != strs[j][n]:
                        p = ""
                        break
                    p += strs[i][n]
                    n += 1
                if len(p) < len(prefix): 
                    break
                prefix = p
        return prefix

    # Attempt 2:
    # Still errors for the string index
    def longestCommonPrefix(self, strs):
        if not strs: 
            return ""
        p = strs[0][0]
        strIdx = 1
        charIdx = 1
        r = len(strs[0]) - 1
        while charIdx <= r and strIdx < len(strs):  
            r = len(strs[strIdx]) - 1 if len(strs[strIdx]) - 1 else r
            print(strs[strIdx][0:charIdx] + " | " + p)
            if strs[strIdx][0:charIdx] == p:
                if len(p) > 1: p += strs[strIdx][charIdx]
                print(p)
                charIdx += 1
            elif strs[strIdx][0] != p[0]: 
                return ""
            else: 
                p = p[0:charIdx-1]
                strIdx += 1
                break    
        return p            
            
lcp = LongestCommonPrefix()
strs = ["flower", "flow", "flight"]
print(lcp.longestCommonPrefix(strs))