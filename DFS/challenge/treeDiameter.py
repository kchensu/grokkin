class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def treeDiameter(root):
    treeDiam = 0

    def treeDiameterRecursive(currNode, treeDiam):
        if currNode is None:
            return 0
        leftHeight = treeDiameterRecursive(currNode.left, treeDiam)
        rightHeight = treeDiameterRecursive(currNode.right, treeDiam)
        diameter = leftHeight + rightHeight + 1
        treeDiam = max(treeDiam, diameter)
        return max(leftHeight, rightHeight) + 1
    return treeDiameterRecursive(root, treeDiam)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print(f"Tree Diameter: {treeDiameter(root)}")


main()
