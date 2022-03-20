class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def binaryTreePathSum(root, sum):
    if root is None:
        return False

    if root.value == sum and root.left is None and root.right is None:
        return True
    leftSum = binaryTreePathSum(root.left, sum - root.value)
    rightSum = binaryTreePathSum(root.left, sum - root.value)

    return leftSum or rightSum


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"Tree has path: {binaryTreePathSum(root, 23)}")
    print(f"Tree has path: {binaryTreePathSum(root, 16)}")


main()
