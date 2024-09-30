# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        string1 = string2 = ""
        node = head
        
        while node is not None:
            string1 += str(node.val)
            string2 = str(node.val) + string2
            node = node.next
            
        return string1 == string2