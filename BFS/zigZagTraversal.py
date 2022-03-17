from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def traverse(root):
    result = []
    queue = deque()
    queue.append(root)
    leftToRight = True
    while queue:
        currLevel = deque()
        for _ in range(len(queue)):
            currNode = queue.popleft()
            if leftToRight:
                currLevel.append(currNode.value)
            else:
                currLevel.appendleft(currNode.value)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

        result.append(list(currLevel))
        leftToRight = not leftToRight

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print(f"Zigzag traversal {traverse(root)}")


main()
