class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class MaximumPathSum:
    def findMaximumPathSum(self, root):
        self.globalMaximumSum = float('-inf')
        self.findMaximumPathSumRecursive(root)
        return self.globalMaximumSum

    def findMaximumPathSumRecursive(self, currNode):
        if currNode is None:
            return 0
        maxLeftSum = self.findMaximumPathSumRecursive(currNode.left)
        maxRightSum = self.findMaximumPathSumRecursive(currNode.right)

        maxLeftSum = max(maxLeftSum, 0)
        maxRightSum = max(maxRightSum, 0)

        currMaxSum = currNode.value + maxLeftSum + maxRightSum
        self.globalMaximumSum = max(self.globalMaximumSum, currMaxSum)
        return max(maxLeftSum, maxRightSum) + currNode.value


def main():
    maxSumPath = MaximumPathSum()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(f"Maximum Path Sum: {maxSumPath.findMaximumPathSum(root)}")


main()
