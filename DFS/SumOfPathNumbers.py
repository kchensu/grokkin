class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def findSumOfPath(root):
    return findRootToLeafSum(root, 0)


def findRootToLeafSum(currNode, pathSum):
    if currNode is None:
        return 0

    pathSum = 10*pathSum + currNode.val
    if currNode.left is None and currNode.right is None:
        return pathSum

    return findRootToLeafSum(currNode.left, pathSum) + findRootToLeafSum(currNode.right, pathSum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print(f"Total Sum of Path Numbers: {findSumOfPath(root)}")


main()
