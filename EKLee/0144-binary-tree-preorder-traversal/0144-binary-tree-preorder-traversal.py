# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, res):
            if not root: return
            res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)
            return res
        if not root: return []
        return dfs(root,[])
        