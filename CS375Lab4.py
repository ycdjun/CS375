# Yongchan Jun and Tristan Awayan


# Object TreeNode
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Input: root, TreeNode p, TreeNode q
# Output: TreeNode lowestCommonAncestor
# Utilizes DFS to recursively traverse the tree
def lowestCommonAncestor(root, p, q):
    if not root:
        return None
    # Check if current node is p or q
    if p == root or q == root:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    if not left:
        return right
    if not right:
        return left


root = TreeNode(1)
root.left = TreeNode(11)
root.left.left = TreeNode(21)
root.left.left.left = TreeNode(28)
root.left.left.right = TreeNode(29)
root.left.right = TreeNode(22)
root.left.right.left = TreeNode(30)
root.left.right.right = TreeNode(31)
root.right = TreeNode(12)
root.right.left = TreeNode(23)
root.right.right = TreeNode(24)
root.right.left.left = TreeNode(32)
root.right.left.right = TreeNode(33)
root.right.right.left = TreeNode(34)
root.right.right.right = TreeNode(35)

print(lowestCommonAncestor(root, root.left.left, root.right.right.left).val)
