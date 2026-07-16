# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast = head.next
        slow = head

        # goes and makes slow the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverses all of the links after the middle with prev pointing to the end
        tmp = slow.next
        slow.next = None
        prev = None

        while tmp:
            nxt = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = nxt
        
        # then you basically have two linked lists and merge them correctly
        curr = head
        while curr and prev:
            c_next = curr.next
            p_next = prev.next
            
            curr.next=prev
            curr = curr.next
            curr.next = c_next
            
            curr = c_next
            prev = p_next


