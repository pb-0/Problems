# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root):  # DFS with stack
        l, res = [root], 0

        while l:

            node = l.pop()

            if not node.left and not node.right:
                res += node.val

            if node.right:
                node.right.val += node.val * 10
                l.append(node.right)

            if node.left:
                node.left.val += node.val * 10
                l.append(node.left)

        return res