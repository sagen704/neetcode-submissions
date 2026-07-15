# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, curr):

        if not curr:
            return 0

        leftHeight = self.dfs(curr.left)
        rightHeight = self.dfs(curr.right)

        self.diameter = max(self.diameter, leftHeight + rightHeight)
        # self.diameter = leftHeight + rightHeight
        return max(leftHeight, rightHeight) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        self.dfs(root)

        return self.diameter


        