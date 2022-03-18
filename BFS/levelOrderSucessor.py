from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findSuccessor(root, key):
    queue = deque()
    queue.append(root)
    while queue:
        currNode = queue.popleft()
        if currNode.left:
            queue.append(currNode.left)

        if currNode.right:
            queue.append(currNode.right)

        if currNode.value == key:
            break

    return queue[0] if queue else None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = findSuccessor(root, 12)
    if result:
        print(result.value)
    result = findSuccessor(root, 9)
    if result:
        print(result.value)


main()
