class Tree:
    data=None
    left=None
    right=None
    def __init__(self,data):
        self.data=data

arr=[]        
        

def inOrder(ptr):
    if ptr==None:
        return None
    else:
        inOrder(ptr.left)
        print(ptr.data)
        inOrder(ptr.right)
        
def inserterElementInArray(ptr):
    if ptr==None:
        return None
    else:
        inserterElementInArray(ptr.left)
        arr.append(ptr.data)
        inserterElementInArray(ptr.right)
        
def isBST(arr):
    flag=False
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            flag=True
        else:
            flag=False
            break
    if flag==True:
        print("It is An Binary Search Tree")
    else:
        print("It is Not A Binary Search Tree")
        
 
def SearchingInBST(ptr,sval):
    if ptr==None:
        return False
    if ptr.data==sval:
        return True
    elif ptr.data>sval:
        return SearchingInBST(ptr.left,sval)
    elif ptr.data<sval:
        return SearchingInBST(ptr.right,sval)
    

    
    
def InsertionInBSt(ptr,data):
    if ptr==None:
        newnode=Tree(data)
        return newnode
    elif ptr.data>data:
        ptr.left=InsertionInBSt(ptr.left,data)
    elif ptr.data<data:
        ptr.right=InsertionInBSt(ptr.right,data)
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

def deletionInBST(ptr,sval):
    if ptr==None:
        return None
    elif ptr.data>sval:
        ptr.left=deletionInBST(ptr.left,sval)
    elif ptr.data<sval:
        ptr.right=deletionInBST(ptr.right,sval)
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
        ptr.right=deletionInBST(ptr.right,temp.data)
        
    return ptr
        
    
        
a=None
a=InsertionInBSt(a,9)
a=InsertionInBSt(a,5)
a=InsertionInBSt(a,18)
a=InsertionInBSt(a,3)
a=InsertionInBSt(a,7)
a=InsertionInBSt(a,13)
a=InsertionInBSt(a,22)
a=InsertionInBSt(a,4)
a=InsertionInBSt(a,14)
a=deletionInBST(a,9)



inOrder(a)