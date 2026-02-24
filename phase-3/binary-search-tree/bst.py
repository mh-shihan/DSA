class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def insertIntoBST(self, root, data):
            if not root:
                return Node(data)

            cur = root

            while True:
                if cur.data < data:
                    if cur.right is not None:
                        cur = cur.right
                    else:
                        cur.right = Node(data)
                        break
                else:
                    if cur.left is not None:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        break

            return root
    
    def search(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True

        if key < root.data:
            self.search(root.left, key)
        else:
            self.search(root.right, key)






# -------- MAIN --------
root = BST().root

n = int(input("How many values do you want to insert? "))

for i in range(n):
    value = int(input(f"Enter value {i+1}: "))
    root = BST().insertIntoBST(root, value)

print("All values inserted successfully!")


# SEARCH
key = int(input("Enter value to search: "))

if BST().search(root, key):
    print(f"{key} found in BST.")
else:
    print(f"{key} not found in BST.")