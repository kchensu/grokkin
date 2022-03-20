class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def countPaths(root, sum):
    return countPathsRecursive(root, sum, [])


def countPathsRecursive(currNode, Sum, currPaths):
    if currNode is None:
        return 0
    currPaths.append(currNode.value)
    pathCount, pathSum = 0, 0
    for i in reversed(range(len(currPaths))):
        pathSum += currPaths[i]
        if pathSum == Sum:
            pathCount += 1
    pathCount += countPathsRecursive(currNode.left, Sum, currPaths)
    pathCount += countPathsRecursive(currNode.right, Sum, currPaths)

    del currPaths[-1]
    return pathCount


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"Tree has paths: {countPaths(root, 11)}")


main()
