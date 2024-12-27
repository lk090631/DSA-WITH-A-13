class Node:
    data=None
    next=None
    def __init__(self,data):
        self.data=data
        
def Traversal(ptr):
    if ptr==None:
        return None
    qtr=ptr
    print(qtr.data)
    qtr=qtr.next
    while qtr!=ptr:
        print(qtr.data)
        qtr=qtr.next
        
def insertionATB(ptr,data):
    if ptr==None:
        newnode=Node(data)
        newnode.next=newnode
        return newnode
    if ptr.next==ptr:
        newnode=Node(data)
        newnode.next=ptr
        ptr.next=newnode
        return newnode
    qtr=ptr
    ftr=qtr.next
    while ftr!=ptr:
        qtr=qtr.next
        ftr=ftr.next
    
    newnode=Node(data)
    newnode.next=ptr
    qtr.next=newnode
    return newnode

def insertionATEND(ptr,data):
    if ptr==None:
        newnode=Node(data)
        newnode.next=newnode
        return newnode
    if ptr.next==ptr:
        newnode=Node(data)
        newnode.next=ptr
        ptr.next=newnode
        return ptr
    qtr=ptr
    ftr=qtr.next
    while ftr!=ptr:
        qtr=qtr.next
        ftr=ftr.next
    
    newnode=Node(data)
    newnode.next=ptr
    qtr.next=newnode
    return ptr
  
def insertionATBT(ptr,data,index):
    if ptr==None:
        newnode=Node(data)
        newnode.next=newnode
        return newnode
    if ptr.next==ptr:
        newnode=Node(data)
        newnode.next=ptr
        ptr.next=newnode
        return newnode
    if index==0:
        return insertionATB(a,data)
    
    count=1
    copyptr=ptr.next
    while copyptr!=ptr:
        count=count+1
        copyptr=copyptr.next
    
    if count>index:
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index-1 and ftr!=ptr:
            qtr=qtr.next
            ftr=ftr.next
            i=i+1
        
        newnode=Node(data)
        newnode.next=ftr
        qtr.next=newnode
        return ptr
    else:
        print("Index Out Of the Range")
        return ptr


def deletionATB(ptr):
    if ptr==None:
        return None
    if ptr.next==ptr:
        return None
    qtr=ptr
    ftr=qtr.next
    while ftr!=ptr:
        ftr=ftr.next
        qtr=qtr.next
    
    qtr.next=ftr.next
    return ftr.next

def deletionATEND(ptr):
    if ptr==None:
        return None
    if ptr.next==ptr:
        return None
    qtr=ptr
    ftr=qtr.next
    while ftr.next!=ptr:
        qtr=qtr.next
        ftr=ftr.next
    qtr.next=ftr.next
    return ptr


def deletionATBT(ptr,index):
    if ptr==None:
        return None
    if index==0:
        if ptr.next==ptr:
            return None
        else:
            return deletionATB(ptr)
    count=1
    copyptr=ptr.next
    while copyptr!=ptr:
        count=count+1
        copyptr=copyptr.next
    
    if count>index:
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index-1 and ftr!=ptr:
            qtr=qtr.next
            ftr=ftr.next
            i=i+1    
        qtr.next=ftr.next
        return ptr
    else:
        print("Index Out Of The Range")
        return ptr
    
def CycleBreak(ptr):
    if ptr.next==ptr:
        ptr.next=None
        return ptr
    qtr=ptr
    ftr=qtr.next
    while ftr!=ptr:
        qtr=qtr.next
        ftr=ftr.next
    qtr.next=None
    return ptr


def AfterCycleBreak_Traversal(ptr):
    while ptr!=None:
        print(ptr.data)
        ptr=ptr.next
            
a=None

a=insertionATEND(a,10)
a=insertionATEND(a,20)
a=insertionATEND(a,30)
a=insertionATEND(a,40)
a=insertionATBT(a,50,2)
a=insertionATBT(a,50,4)
a=insertionATBT(a,60,0)

Traversal(a)
a=CycleBreak(a)
print()
AfterCycleBreak_Traversal(a)





        