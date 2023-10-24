# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
       def largestValues(self, root: Optional[TreeNode]):
        Q = deque([root]) if root else ()
        while Q:
            yield max(x.val for x in Q)
            for _ in range(len(Q)):
                x = Q.popleft()
                Q += (y for y in (x.left, x.right) if y)