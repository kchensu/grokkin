class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def findPath(root, sequence):
    return findPathRecursive(root, sequence, 0)


def findPathRecursive(currNode, sequence, idx):
    if currNode is None:
        return False

    if idx >= len(sequence) or currNode.val != sequence[idx]:
        return False
    if currNode.left is None and currNode.right is None and idx == len(sequence) - 1:
        return True

    return findPathRecursive(currNode.left, sequence, idx + 1) or findPathRecursive(currNode.right, sequence, idx + 1)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print(f"Tree has path sequence: {findPath(root, [1,0,7])}")
    print(f"Tree has path sequence: {findPath(root, [1,1,6])}")


main()
