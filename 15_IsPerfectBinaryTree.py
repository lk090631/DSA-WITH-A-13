class Tree:
    data=None
    left=None
    right=None
    
    def __init__(self,data):
        self.data=data
        
def preOrder(ptr):
    if ptr==None:
        return None
    else:
        print(ptr.data)
        preOrder(ptr.left)
        preOrder(ptr.right)
        
def inOrder(ptr):
    if ptr==None:
        return None
    else:
        inOrder(ptr.left)
        print(ptr.data)
        inOrder(ptr.right)

def postOrder(ptr):
    if ptr==None:
        return None
    else:
        postOrder(ptr.left)
        postOrder(ptr.right)
        print(ptr.data)
        
def count_height(ptr,h=0):
    if ptr==None:
        return h
    else:
        return max(count_height(ptr.left,h+1),count_height(ptr.right,h+1))


def isPerfectBinaryTree(ptr,height,level=0):
    if ptr==None:
        return True
    elif ptr.left==None and ptr.right==None:
        return height==level+1
    
    elif ptr.left==None or ptr.right==None:
        return False
    
    return isPerfectBinaryTree(ptr.left,height,level+1) and isPerfectBinaryTree(ptr.right,height,level+1)
    
        
    
    
a=Tree(10)
b=Tree(20)
c=Tree(30)
d=Tree(40)
e=Tree(50)
f=Tree(60)
g=Tree(70)


a.left=b
a.right=c

b.left=d
b.right=e

c.left=f
c.right=g


total=count_height(a)

if isPerfectBinaryTree(a,total):
    print("It is Perfect Binary Tree")
else:
    print("It is Not A Pefect Binary Tree")
