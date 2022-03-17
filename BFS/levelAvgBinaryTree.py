from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def levelAverageBinaryTree(root):
    result = []
    queue = deque()
    queue.append(root)
    while queue:
        levelSum = 0.0
        lenght = len(queue)
        for _ in range(len(queue)):

            currNode = queue.popleft()
            levelSum += currNode.value

            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
        averageLevel = levelSum/lenght
        result.append(averageLevel)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(f"Level average are: {levelAverageBinaryTree(root)}")


main()
