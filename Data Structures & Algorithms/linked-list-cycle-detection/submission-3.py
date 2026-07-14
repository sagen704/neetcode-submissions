# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        nodes_visited = set()

        curr = head

        while curr:
            print(curr, nodes_visited)
            if curr in nodes_visited:
                return True
            nodes_visited.add(curr)
            curr = curr.next

        return False
        