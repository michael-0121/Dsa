class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def diff(root, min_val, max_val):
            if not root:
                return True
            if (min_val is not None and root.val <= min_val) or (
                max_val is not None and root.val >= max_val
            ):
                return False
            return diff(root.left, min_val, root.val) and diff(
                root.right, root.val, max_val
            )

        return diff(root, None, None)