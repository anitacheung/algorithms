# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ptr = head
        total = 0
        
        if ptr == None:
            return False
        
        while (ptr.next != None):
            if (hasattr(ptr, 'pos')):
                return True
            else:
                ptr.pos = total
            
            ptr = ptr.next
            total += 1
        
        return False
    
    
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Two pointer is not as fast but uses significantly less memory.
        """
        fast = head
        slow = head
        
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False
        