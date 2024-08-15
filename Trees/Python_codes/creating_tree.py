#creating  the Node Class for the tree
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
#creating the first tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
print(root.value)
