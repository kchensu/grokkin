from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def treeRightView(root):
    res = []
    queue = deque()
    queue.append(root)
    while queue:
        length = len(queue)
        for i in range(length):
            currNode = queue.popleft()
            # append to result if the curr node is the last level node.
            if i == length - 1:
                res.append(currNode)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
    return res


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    res = treeRightView(root)
    print(f"Tree Right View:")
    for node in res:
        print(f"{node.value}", end=" ")


main()
