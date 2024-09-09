# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        output = []
        
        def dfs(node):
            if node:
                dfs(node.left) # 왼쪽 먼저 탐색해준 후
                output.append(node.val) # 현재 val 탐색 후
                dfs(node.right) # 오른쪽을 또 탐색해줌
                
        dfs(root)
        return output