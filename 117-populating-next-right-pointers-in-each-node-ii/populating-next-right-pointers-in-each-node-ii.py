"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return None 

        Que = collections.deque()
        Que.append(root)

        while Que :
            l = len (Que)
            prev = None 

            for _ in range(l):
                curr = Que.popleft()

                if prev:
                    prev.next = curr

                prev = curr
                if curr.left:
                    Que.append(curr.left)

                if curr.right:
                    Que.append(curr.right)

        return root