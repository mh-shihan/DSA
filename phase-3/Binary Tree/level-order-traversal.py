from collections import deque

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

def levelOrder(root):
    ans = []
    if root is None:
        return ans
    
    q = deque([root])
    
    while q:
        size = len(q)
        level = []
        
        for i in range(size):
            node = q.popleft()
            
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            
            level.append(node.data)
        
        ans.append(level)
    
    return ans

rootNode = build_tree()
levels = levelOrder(rootNode)

totalLevels = len(levels)

for i, level in enumerate(levels):
    spaces = " " * (2 ** (totalLevels - i))
    print(spaces + str(level))
