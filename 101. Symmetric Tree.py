# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetry(self, left, right) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False

        if left.val == right.val and self.checkSymmetry(left.left, right.right) and self.checkSymmetry(left.right, right.left):
            return True

        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.checkSymmetry(root.left, root.right)
