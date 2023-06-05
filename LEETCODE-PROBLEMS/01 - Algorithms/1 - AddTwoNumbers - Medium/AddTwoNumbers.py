# You are given two non-empty linked lists representing 
# two non-negative integers. The digits are stored in reverse order, 
# and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, 
# except the number 0 itself.

# Example 1:

# (2)---->(4)---->(3)
# (2)---->(4)---->(3)
# -------------------
# (2)---->(4)---->(3)

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddTwoNumbers(object):   
    
    # this approach works only for arrays or lists.
    # needs different method for linked lists
    def addTwoNums(self, l1, l2): 
        res = []
        n1 = int(''.join(str(e) for e in reversed(l1)))
        n2 = int(''.join(str(e) for e in reversed(l2)))
        n3 = str(n1 + n2)
        for i in range(len(str(n3)) - 1, -1, -1):
            res.append(int(n3[i]))
        return res
    
    # fix later
    def addTwoNums_2(self, l1, l2):
        rev_l1 = []
        current = l1
        while current:
            rev_l1.append(current.val)
            current = current.next
        return rev_l1

#------------------ TEST ------------------

# Create linked lists
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

atn = AddTwoNumbers()
result = atn.addTwoNums_2(l1, l2)
print(result)
        