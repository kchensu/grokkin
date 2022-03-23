class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def treeDiameter(root):
    treeDiam = [0]

    def treeDiameterRecursive(currNode):
        if currNode is None:
            return 0
        leftHeight = treeDiameterRecursive(currNode.left)
        rightHeight = treeDiameterRecursive(currNode.right)
        diameter = leftHeight + rightHeight + 1
        treeDiam[0] = max(treeDiam[0], diameter)
        return max(leftHeight, rightHeight) + 1
    treeDiameterRecursive(root)
    return treeDiam[0]


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print(f"Tree Diameter: {treeDiameter(root)}")


main()
