from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def traverse(root):
    result = deque()

    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        currLevel = []
        for _ in range(len(queue)):
            currNode = queue.popleft()
            currLevel.append(currNode.value)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
        result.appendleft(currLevel)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"Reverse order traversal {traverse(root)}")


main()
