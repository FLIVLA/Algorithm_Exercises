"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeSortedLists(object):
    
    # Not working for linked list, though
    # seems fine for ordinary list.
    # Time Complexity: Linear | O(m+n) where m is length 
    # of list1 and n is length of list2
    def merge(self, list1, list2):
        if len(list1) <= 1: 
            return list2
        elif len(list2) <= 1:
            return list1
        res = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]: 
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1
        res.extend(list1[i:])
        res.extend(list2[j:])
        return res
    
    # Working for linked lists.
    def merge_linked(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next 
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return dummy.next
        


#------------------ TEST ------------------

list1 = [1,2,4] 
list2 = [1,3,4]

m = MergeSortedLists()
print(m.merge(list1, list2))
        