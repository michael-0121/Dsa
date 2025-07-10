class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs (root,cur):
            if not root:
                return False 
            cur += root.val

            if not root.left and not root.right:
                if cur == targetSum:
                    return True
            return dfs(root.left,cur) or dfs (root.right,cur)
        return dfs(root,0)