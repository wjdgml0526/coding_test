/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode fast, slow;
        fast = slow = head;

        while (fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) break;
        }
        
        if (fast == null || fast.next == null) return null;
        // fast는 지금 만났던 지점인데
        // 먼저 하나의 포인터가 다시 head를 가리킴
        while (head != slow) {
            // 두 포인터는 이제 같은 속도로 이동
            head = head.next;
            slow = slow.next;
        }       
        // 만나는 지점이 순환기점
        return head;
    }
}