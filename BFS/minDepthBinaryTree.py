from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def minDepthBinaryTree(root):
    result = []
    queue = deque()
    minDepthLength = 0
    queue.append(root)
    while queue:
        minDepthLength += 1
        for _ in range(len(queue)):
            currNode = queue.popleft()
            if currNode.left is None and currNode.right is None:
                return minDepthLength
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

    return minDepthLength


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"Tree Mininum Depth: {minDepthBinaryTree(root)}")
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print(f"Tree Mininum Depth: {minDepthBinaryTree(root)}")


main()
