class FindIdxOfFirst(object):
    
    # home made stuff 
    def findIdx(self, haystack, n):
        if haystack == n: 
            return 0
        nR = len(n) if len(n) > 1 else 1     # Initialize boundary
        idx = 0                              # current index
        while nR <= len(haystack):           # loop until nR reaches end of haystack
            if haystack[idx:nR] == n:   
                return idx                   # return the index of the n occurence in haystack   
            idx += 1                         # increment idx if no match found
            nR += 1
        return -1                            # in case of no occurences return -1

    # not sure if this is faster?
    def findIdx_2(self, haystack, n):
        if n not in haystack:
            return -1
        else:
            return(haystack.find(n))
        
#------------- TEST ---------------

fif = FindIdxOfFirst()
haystack = "leetcode" 
needle = "leeto"
print(fif.findIdx(haystack, needle))