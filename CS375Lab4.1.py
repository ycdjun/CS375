class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Input: TreeNode s, TreeNode t
# Output: Boolean
# Check if the subTrees are the same
def checkSame(s, t):
    if s is None or t is None:
        return s is None and t is None

    elif s.val == t.val:
        return checkSame(s.left, t.left) and checkSame(s.right, t.right)
    else:
        return False

# Input TreeNode s, TreeNode t
# Output: Boolean
# recursively checks until the subtree is found or there does not exist anymore nodes in S


def helper(s, t):
    if s is None:
        return False
    elif checkSame(s, t):
        return True
    else:
        return helper(s.left, t) or helper(s.right, t)


def isSubtree(s, t):
    return helper(s, t)


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
root.right.left.left.left = TreeNode(34)
root.right.left.right = TreeNode(33)
root.right.right.right = TreeNode(35)

subTreeNode = TreeNode(23)
subTreeNode.left = TreeNode(100)
subTreeNode.right = TreeNode(33)
subTreeNode.left.left = TreeNode(34)


print(isSubtree(root, subTreeNode))
