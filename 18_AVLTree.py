class Tree:
    data=None
    left=None
    right=None
    height=1
    def __init__(self,data):
        self.data=data
        

def inOrder(ptr):
    if ptr==None:
        return None
    else:
        inOrder(ptr.left)
        print(ptr.data)
        inOrder(ptr.right)
        
def getheight(ptr):
    if ptr==None:
        return 0
    else:
        return ptr.height
    
def getBalanceFactor(ptr):
    if ptr==None:
        return 0
    else:
        return getheight(ptr.left)-getheight(ptr.right)
    
    
def rightrotation(y):
    x=y.left
    t2=x.right
    x.right=y
    y.left=t2
    
    y.height=max(getheight(y.left),getheight(y.right))+1
    x.height=max(getheight(x.left),getheight(x.right))+1
    return x


def leftrotation(x):
    y=x.right
    t2=y.left
    y.left=x
    x.right=t2
    
    y.height=max(getheight(y.left),getheight(y.right))+1
    x.height=max(getheight(x.left),getheight(x.right))+1
    return y
    
    
        
        
        
def SearchingInBST(ptr,sval):
    if ptr==None:
        return False
    if ptr.data==sval:
        return True
    elif ptr.data>sval:
        return SearchingInBST(ptr.left,sval)
    elif ptr.data<sval:
        return SearchingInBST(ptr.right,sval)
    
    
def InsertionInAVL(ptr,data):
    if ptr==None:
        newnode=Tree(data)
        return newnode
    elif ptr.data>data:
        ptr.left=InsertionInAVL(ptr.left,data)
    elif ptr.data<data:
        ptr.right=InsertionInAVL(ptr.right,data)
        
        
    ptr.height=1+max(getheight(ptr.left),getheight(ptr.right))
    balance=getBalanceFactor(ptr)
    
    if balance>1:
        if getBalanceFactor(ptr.left)>=0:
            return rightrotation(ptr)
        else:
            ptr.left=leftrotation(ptr.left)
            return rightrotation(ptr)
        
        
    if balance<-1:
        if getBalanceFactor(ptr.right)<=0:
            return leftrotation(ptr)
        else:
            ptr.right=rightrotation(ptr.right)
            return leftrotation(ptr)
    return ptr

def Predecessor(ptr):
    qtr=ptr
    while qtr.right!=None:
        qtr=qtr.right
    return qtr

def Successor(ptr):
    qtr=ptr
    while qtr.left!=None:
        qtr=qtr.left
    return qtr


def deletionInAVL(ptr,sval):
    if ptr==None:
        return None
    elif ptr.data>sval:
        ptr.left=deletionInAVL(ptr.left,sval)
    elif ptr.data<sval:
        ptr.right=deletionInAVL(ptr.right,sval)
    else:
        if ptr.left==None:
            temp=ptr.right
            ptr=None
            return temp
        if ptr.right==None:
            temp=ptr.left
            ptr=None
        temp=Successor(ptr.right)
        ptr.data=temp.data
        ptr.right=deletionInAVL(ptr.right,temp.data)
    
    ptr.height=1+max(getheight(ptr.left),getheight(ptr.right))
    balance=getBalanceFactor(ptr)
    
    if balance>1:
        if getBalanceFactor(ptr.left)>=0:
            return rightrotation(ptr)
        else:
            ptr.left=leftrotation(ptr.left)
            return rightrotation(ptr)
        
        
    if balance<-1:
        if getBalanceFactor(ptr.right)<=0:
            return leftrotation(ptr)
        else:
            ptr.right=rightrotation(ptr.right)
            return leftrotation(ptr)    
    return ptr

a=None
a=InsertionInAVL(a,50)
a=InsertionInAVL(a,27)
a=InsertionInAVL(a,77)
a=InsertionInAVL(a,67)
a=InsertionInAVL(a,65)
a=InsertionInAVL(a,21)
a=InsertionInAVL(a,23)
a=InsertionInAVL(a,25)

inOrder(a)