# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        exp = 1
        # l1, l2로 부터 각 자연수를 추출해서 뒤집기
        while l1 is not None:
            num1 += exp * l1.val
            l1 = l1.next
            exp *= 10
        
        exp = 1
        while l2 is not None:
            num2 += exp *l2.val
            l2 = l2.next
            exp *= 10
        
        # 더하기
        num = num1 + num2
        
        # ListNode로 뒤집어 재분배하기
        dummy = ListNode()
        cur = dummy

        if num != 0 :
            while num > 0 :
                mod = num % 10
                num //= 10 

                cur.next = ListNode(mod)
                cur = cur.next
        else : # num == 0
            dummy.next = ListNode()

        return dummy.next