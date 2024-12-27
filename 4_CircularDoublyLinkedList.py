class Node:
    data=None
    prev=None
    next=None
    def __init__(self,data):
        self.data=data

def Traversal(ptr):
    if ptr==None:
        return None
    if ptr.next==ptr and ptr.prev==ptr:
        print(ptr.data)
        return ptr
    qtr=ptr
    print(qtr.data)
    qtr=qtr.next
    while qtr!=ptr:
        print(qtr.data)
        qtr=qtr.next
        
def Traversal_Reverse(ptr):
    if ptr==None:
        return None
    if ptr.next==ptr and ptr.prev==ptr:
        print(ptr.data)
        return ptr
    qtr=ptr
    qtr=qtr.prev  
    while qtr!=ptr:
        print(qtr.data)
        qtr=qtr.prev
    print(ptr.data)
    
def insertionATB(ptr,data):
    if ptr==None:
        newnode=Node(data)
        newnode.next=newnode
        newnode.prev=newnode
        return newnode
    if ptr.next==ptr and ptr.prev==ptr:
        newnode=Node(data)
        newnode.next=ptr
        newnode.prev=ptr
        ptr.next=newnode
        ptr.prev=newnode
        return newnode
    qtr=ptr
    ftr=qtr.next
    while ftr!=ptr:
        qtr=qtr.next
        ftr=ftr.next
    newnode=Node(data)
    newnode.next=ftr
    newnode.prev=qtr
    qtr.next=newnode
    ftr.prev=newnode
    return newnode
    
def insertionATEND(ptr,data):
    if ptr==None:
        newnode=Node(data)
        newnode.next=newnode
        newnode.prev=newnode
        return newnode
    if ptr.next==ptr and ptr.prev==ptr:
        newnode=Node(data)
        newnode.next=ptr
        newnode.prev=ptr
        ptr.next=newnode
        ptr.prev=newnode
        return ptr
    qtr=ptr
    ftr=qtr.next
    while ftr!=ptr:
        qtr=qtr.next
        ftr=ftr.next
    newnode=Node(data)
    newnode.next=ftr
    newnode.prev=qtr
    qtr.next=newnode
    ftr.prev=newnode
    return ptr       
 
def insertionATBT(ptr,data,index):
    if ptr==None:
        return insertionATB(ptr,data)
    if index==0:
        return insertionATB(ptr,data)
    count=1
    copyptr=ptr
    copyptr=copyptr.next
    while copyptr!=ptr:
        count=count+1
        copyptr=copyptr.next
        
    if count>index:
            
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index-1 and ftr!=ptr:
            ftr=ftr.next
            qtr=qtr.next   
            i=i+1
        newnode=Node(data)
        newnode.next=ftr
        newnode.prev=qtr
        qtr.next=newnode
        ftr.prev=newnode
        return ptr
    else:
        print("Index Out Of The Range")
        return ptr 
    
def deletionATB(ptr):
    if ptr==None:
        return None
    if ptr.next==ptr and ptr.prev==ptr:
        return None
    qtr=ptr
    ftr=qtr.next
    while ftr!=ptr:
        qtr=qtr.next
        ftr=ftr.next
    qtr.next=ftr.next
    ftr.next.prev=qtr
    return ftr.next

def deletionATEND(ptr):
    if ptr==None:
        return None
    if ptr.next==ptr and ptr.prev==ptr:
        return None
    qtr=ptr
    ftr=qtr.next
    while ftr.next!=ptr:
        qtr=qtr.next
        ftr=ftr.next
    qtr.next=ftr.next
    ftr.next.prev=qtr
    return ftr.next

def deletionATBT(ptr,index):
    if ptr==None:
        return None
    if index==0:
        return None
    count=1
    copyptr=ptr
    copyptr=copyptr.next
    while copyptr!=None:
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
        ftr.next.prev=qtr
        return ptr
    else:
        print("Index Out Of The Range")
        return ptr   
            
a=None
a=insertionATEND(a,10)
a=insertionATEND(a,20)
a=insertionATEND(a,30)
a=insertionATEND(a,40)

a=deletionATEND(a)
Traversal(a)