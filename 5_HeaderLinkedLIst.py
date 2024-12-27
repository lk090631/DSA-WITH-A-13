class Node:
    data=None
    next=None
    def __init__(self,data):
        self.data=data

def Traversal(ptr):
    while ptr!=None:
        print(ptr.data)
        ptr=ptr.next        

def insertionATB(ptr,data):
    if ptr==None:
        newnode=Node(0)
        newnode.next=None
        return newnode
    
    if ptr.next==None:
        newnode=Node(data)
        ptr.next=newnode
        ptr.data=ptr.data+1
        return ptr
        
    newnode=Node(data)
    newnode.next=ptr.next
    ptr.next=newnode
    ptr.data=ptr.data+1
    return ptr

def insertionATEND(ptr,data):
    if ptr==None:
        newnode=Node(0)
        newnode.next=None
        return newnode
    if ptr.next==None:
        newnode=Node(data)
        newnode.next=None
        ptr.next=newnode
        ptr.data=ptr.data+1
        return ptr
    qtr=ptr
    ftr=qtr.next
    while ftr!=None:
        ftr=ftr.next
        qtr=qtr.next
    newnode=Node(data)
    newnode.next=None
    qtr.next=newnode
    ptr.data=ptr.data+1
    return ptr

def insertionATBT(ptr,data,index):
    if ptr==None:
        newnode=Node(0)
        newnode.next=None
        return newnode
    if ptr.next==None:
        newnode=Node(data)
        newnode.next=None
        ptr.next=newnode
        ptr.data=ptr.data+1
        return ptr
    if index==0:
        newnode=Node(data)
        ptr.next=newnode
        ptr.data=ptr.data+1
        return ptr
    count=0
    copyptr=ptr.next
    while copyptr!=None:
        count=count+1
        copyptr=copyptr.next
    
    if count>index:
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index:
            qtr=qtr.next
            ftr=ftr.next
            i=i+1
        newnode=Node(data)
        newnode.next=ftr
        qtr.next=newnode
        ptr.data=ptr.data+1
        return ptr
    else:
        print("Index Out Of The Range")
        return ptr
    
def deletionATB(ptr):
    if ptr==None:
        return None
    if ptr.next==None:
        return ptr
    qtr=ptr.next
    ptr.next=qtr.next
    ptr.data=ptr.data-1
    return ptr

def deletionATEND(ptr):
    if ptr==None:
        return None
    if ptr.next==None:
        return ptr
    qtr=ptr
    ftr=qtr.next
    while ftr.next!=None:
        ftr=ftr.next
        qtr=qtr.next
    qtr.next=ftr.next
    ptr.data=ptr.data-1
    return ptr

def deletionATBT(ptr,index):
    if ptr==None:
        return None
    if ptr.next==None:
        return ptr
    if index==0:
        return ptr
    
    count=0
    copyptr=ptr.next
    while copyptr!=None:
        count=count+1
        copyptr=copyptr.next
    
    if count>index:
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index:
            qtr=qtr.next
            ftr=ftr.next
            i=i+1
        
        qtr.next=ftr.next
        ptr.data=ptr.data-1
        return ptr 
    else:
        print("Index Out Of The Range")
        return ptr


        
header=None
header=insertionATEND(header,10)
header=insertionATEND(header,10)
header=insertionATEND(header,20)
header=insertionATEND(header,30)
header=insertionATBT(header,40,1)
header=insertionATBT(header,50,3)
header=deletionATB(header)

header=deletionATEND(header)
header=deletionATBT(header,2)
Traversal(header)