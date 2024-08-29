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

#traversal in the tree
#1)DFS of three types:
    #a) In-order (Left, Root, Right)
    #b) Pre-order (Root, Left, Right)
    #c) Post-order (Left, Right, Root)

def traverse(node,type="In-order"):
    if(type == "In-order"):
        if(node== None):
            return
        traverse(node.left,type)
        print(node.value, end = " ")
        traverse(node.right,type)
    elif(type == "Pre-order"):
        if(node== None):
            return
        print(node.value, end = " ")
        traverse(node.left,type)
        traverse(node.right,type)
    elif(type == "Post-order"):
        if(node== None):
            return
        traverse(node.left,type)
        traverse(node.right,type)
        print(node.value, end = " ")
    else:
        print("Invalid type of traversal")
        
traverse(root,type="In-order")
print()
traverse(root,type="Post-order")
print()
traverse(root,type="Pre-order")