class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    data = int(input("Enter the data: "))

    if data == -1:
        return None

    root = Node(data)

    print("Enter data for inserting in left:")
    root.left = build_tree()

    print("Enter data for inserting in right:")
    root.right = build_tree()

    return root

def maxDepth(root):
    if root is None:
        return 0

    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)

    return 1 + max(leftDepth, rightDepth)

if __name__ == "__main__":
    print("Build the tree:")
    root = build_tree()

    depth = maxDepth(root)
    print("Maximum depth of the binary tree is:", depth)