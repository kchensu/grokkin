from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

    def printTree(self):
        print(f"Traversal using next pointer: ", end='')
        current = self
        while current:
            print(f"{current.value} ", end="")
            current = current.next


def connectAllSiblings(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    currNode = None
    prevNode = None
    while queue:
        currNode = queue.popleft()
        if prevNode:
            prevNode.next = currNode
        prevNode = currNode

        if currNode.left:
            queue.append(currNode.left)
        if currNode.right:
            queue.append(currNode.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connectAllSiblings(root)
    root.printTree()


main()
