def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    def balanced(p, q)
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return balanced(p.left, q.left) and balanced(p.right, q.right)
    return balanced(p, q)