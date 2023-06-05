# Given an integer x, return true if x is a 
# palindrome, and false otherwise.

# the general approach is to use slicing
# for reading the string backwards to compare with input

class PalindromeNumber(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]: return True
        return False
    
    def isPalindrome_evenMoreClean(self, x):
        return str(x)==str(x)[::-1]