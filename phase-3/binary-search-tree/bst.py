class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    # Find the maximum value in the BST
    def findMaximum(self, root):
        while root.right != None:
            root = root.right
        return root

    # Find the minimum value in the BST
    def findMinimum(self, root):
        while root.left != None:
            root = root.left
        return root

    # Insert a new value into the BST    
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
    
    # Delete a value from the BST
    def deleteNode(self, root, key):
        if root is None:
            return None
        
        if root.data == key:
            return self.helper(root)
        
        # Keep a reference to the original root to return later
        dummy = root
        
        while root is not None:
            if  key < root.data:
                if root.left is not None and root.left.data == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right is not None and root.right.data == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
        
        return dummy

    def helper(self, root):  
        # Case 1: No left child - return right child
        if root.left is None:
            return root.right
        
        # Case 2: No right child - return left child
        elif root.right is None:
            return root.left
        
        # Case 3: Node has both children
        # Store the right child
        rightChild = root.right
        
        # Find the rightmost node in the left subtree
        lastRight = self.findLastRight(root.left)
        
        # Attach the right child to the rightmost node of left subtree
        lastRight.right = rightChild
        
        # Return left child as the new root of this subtree
        return root.left

    def findLastRight(self, root):
        if root.right is None:
            return root
        return self.findLastRight(root.right)
    
    def search(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)






# -------- MAIN --------
root = BST().root

n = int(input("How many values do you want to insert? "))

for i in range(n):
    value = int(input(f"Enter value {i+1}: "))
    root = BST().insertIntoBST(root, value)

print("All values inserted successfully!")


deleteValue = int(input("Enter a value to delete: "))
root = BST().deleteNode(root, deleteValue)


# SEARCH
numberOfSearches = int(input("How many values do you want to search: "))
for i in range(numberOfSearches):
    value = int(input(f"Enter value to search {i+1}: "))
    found = BST().search(root, value)
    if found:
        print(f"{value} found in the BST.")
    else:
        print(f"{value} not found in the BST.")