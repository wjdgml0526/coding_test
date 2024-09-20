# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        # dummy - head 제거를 용이하게 하려고
        dummy.next = head
        # n번째를 제거 -> n-1, n+1을 이어주는 아이디어
        # 투포인터를 활용
        first = dummy
        second = dummy

        for i in range(n+1):
            second = second.next

        while second is not None:
            first = first.next
            second = second.next
        
        first.next = first.next.next

        return dummy.next
        # return head #로 하면 안된다. head제거가 안된다.