
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


def postOrder(root):
    """DFS Post-order traversal: Left -> Right -> Root"""
    if root is None:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=" ")



root = build_tree()
print("Binary Tree is built successfully.")
print("\nDFS Post-order Traversal:")
postOrder(root)
print()
