class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findPaths(root, sum):
    return findPathRecursive(root, sum, [], [])


def findPathRecursive(currNode, sum, currPath, allPaths):
    if currNode is None:
        return
    currPath.append(currNode.value)
    if currNode.value == sum:
        allPaths.append(list(currPath))
    else:
        findPathRecursive(currNode.left, sum -
                          currNode.value, currPath, allPaths)
        findPathRecursive(currNode.right, sum -
                          currNode.value, currPath, allPaths)

    del currPath[-1]
    return allPaths


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(f"{findPaths(root, 23)}")


main()
