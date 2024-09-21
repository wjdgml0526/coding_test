# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # cur, prv, nxt의 포인터를 활용
        cur = head
        prv = None

        while cur is not None : 
            # reverse처리
            nxt = cur.next
            cur.next = prv

            # 이동
            prv = cur
            cur = nxt
            
        
        return prv