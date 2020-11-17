class TreeNode():
    def __init__(self,root,left=None,right=None):
        self.root = root
        self.left = left
        self.right = right

def preorder(r):
    print(r.root)
    if r.left:
        preorder(r.left)
    if r.right:
        preorder(r.right)

def inorder(r):
    if r.left:
        inorder(r.left)
    print(r.root)
    if r.right:
        inorder(r.right)

def baorder(r):
    if r.left:
        baorder(r.left)
    if r.right:
        baorder(r.right)
    print(r.root)
    
A = TreeNode(5000)
B = TreeNode(10)
C = TreeNode(300)
D = TreeNode(500)
E = TreeNode(6000)
F = TreeNode(80)
G = TreeNode(30)

A.left = B
B.left = C
B.right = D
A.right = E
E.left = F
E.right = G
print('pre:')
preorder(A)

print('in:')
inorder(A)

print('ba:')
baorder(A)


