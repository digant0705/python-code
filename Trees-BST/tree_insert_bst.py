class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
    
def insert(root,Node):
    if root.val is None:
        root=Node
        print(f"inserted-->root {Node.val}")
        return True

    elif root.val<Node.val:
        if root.right is None:
            root.right=Node
            print(f"inserted-->node {Node.val}")
            return True
        else:
            insert(root.right,Node)
    
    elif root.val>Node.val:
        if root.left is None:
            root.left=Node
            print(f"inserted-->node {Node.val}")
            return True
        else:
            insert(root.left,Node)

root=Node(10)
print(f"inserted-->root {root.val}")
insert(root,Node(8))
insert(root,Node(12))
insert(root,Node(6))
insert(root,Node(9))
insert(root,Node(11))
insert(root,Node(13))
insert(root,Node(14))

"""
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right)
inorder(root)
"""

#inorder taversal left->root->right
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val,end=" ")
    inorder_traversal(root.right)

inorder_traversal(root)
print("")

#preorder traversal root->left->rightgit
def preorder_traversal(root):
    if root:
        print(root.val,end=" ")
    else:
        print(-1,end=" ")
        return
    preorder_traversal(root.left)
    preorder_traversal(root.right)

preorder_traversal(root)
print("")

#postorder traversal left->right->root

def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val,end=" ")

postorder_traversal(root)

    
