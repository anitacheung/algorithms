/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(-1);
        ListNode dummyIt = dummy;
        int carry = 0;

        while (l1 != null || l2 != null || carry > 0) {
            int val = carry;
            val += l1 != null ? l1.val : 0;
            val += l2 != null ? l2.val : 0;
            carry = val/10;
            val = val %10;
            dummyIt.next = new ListNode(val);
            dummyIt = dummyIt.next;
            l1 = l1 != null ? l1.next: null;
            l2 = l2 != null ? l2.next : null;
        }
        return dummy.next;
    }
}