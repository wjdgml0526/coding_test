"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Hashmap
        origToNew = {}

        # using DFS
        def dfs(node: Optional['Node']) :
            # 이미 복사본이 존재한다면
            if node in origToNew :
                return origToNew[node]
            
            # 값 복사를 진행
            copy = Node(node.val)
            origToNew[node] = copy
            # 인접 값 복사
            for neighbor in node.neighbors :
                copy.neighbors.append(dfs(neighbor))
            # 결과 반환
            return copy
        
        return dfs(node) if node else None

