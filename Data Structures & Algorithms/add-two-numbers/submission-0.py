# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2:
            if l1 and l2:
                print(f'l1.val = {l1.val} , l2.val = {l2.val}')
                number = (l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                number = l1.val
                l1 = l1.next
            else:
                number = l2.val
                l2 = l2.next

            digit = number % 10
            carry = number // 10
            curr.next = ListNode(digit)
            curr = curr.next
            # print(f"adding {digit}, carry = {carry}")

            if l1:
                l1.val = l1.val + carry
            elif l2:
                l2.val = l2.val + carry

        if carry == 1:
            curr.next = ListNode(1)

        return dummy.next
        