class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def height(root):
    if root is None:
        return -1
    return max(height(root.left), height(root.right)) + 1


# Creating the tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.right.left = Node(50)
root.right.right = Node(60)
root.right.left.left = Node(70)

print("Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)

print("\nHeight of tree:")
print(height(root))
