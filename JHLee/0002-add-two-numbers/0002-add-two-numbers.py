# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = dummy = ListNode()

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1
            v2 = l2.val if l2

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)