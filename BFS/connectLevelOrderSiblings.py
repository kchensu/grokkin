from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

    def printTree(self):
        nextLevelRoot = self
        while nextLevelRoot:
            curr = nextLevelRoot
            nextLevelRoot = None
            while curr:
                print(f"{curr.value} ", end="")
                if not nextLevelRoot:
                    if curr.left:
                        nextLevelRoot = curr.left
                    elif curr.right:
                        nextLevelRoot = curr.right
                curr = curr.next
            print()


def connectLevelOrderSiblings(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    while queue:
        prevNode = None
        for _ in range(len(queue)):
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
    connectLevelOrderSiblings(root)
    root.printTree()


main()
