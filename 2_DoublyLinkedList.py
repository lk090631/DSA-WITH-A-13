class Node:
    prev=None
    data=None
    next=None
    def __init__(self,data):
        self.data=data
        

def Traversal(ptr):
    while ptr!=None:
        print(ptr.data)
        ptr=ptr.next
        
def Traversal_Reverse(ptr):
    if ptr==None:
        return None
    while ptr.next!=None:
        ptr=ptr.next
    
    while ptr!=None:
        print(ptr.data)
        ptr=ptr.prev

def insertionATB(ptr,data):
    newnode=Node(data)
    newnode.next=ptr
    newnode.prev=None
    ptr.prev=newnode
    return newnode

def insertionATEND(ptr,data):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
        newnode.prev=None
        ptr.prev=newnode
        return newnode    
    qtr=ptr
    while qtr.next!=None:
        qtr=qtr.next
    newnode=Node(data)
    newnode.next=None
    newnode.prev=qtr
    qtr.next=newnode
    return ptr


def insertionATBT(ptr,data,index):
    if ptr==None or index==0:
        newnode=Node(data)
        newnode.next=ptr
        newnode.prev=None
        ptr.prev=newnode
        return newnode 
    count=0
    copyptr=ptr
    while copyptr!=None:
        count=count+1
        copyptr=copyptr.next
        
    if count>index:    
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index-1:
            qtr=qtr.next
            ftr=ftr.next
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
    

def insertionATSVB(ptr,data,sval):
    if ptr==None or ptr.data==sval:
        newnode=Node(data)
        newnode.next=ptr
        newnode.prev=None
        ptr.prev=newnode
        return newnode
    
    flag=False
    copyptr=ptr
    while copyptr!=None:
        if copyptr.data==sval:
            flag=True
            break
        else:
            flag=False
        copyptr=copyptr.next
        
    if flag==True:    
        qtr=ptr
        ftr=qtr.next
        while ftr.data!=sval:
            qtr=qtr.next
            ftr=ftr.next
        
        newnode=Node(data)
        newnode.next=ftr
        newnode.prev=qtr
        qtr.next=newnode
        ftr.prev=newnode
        return ptr
    else:
        print("Search Value Does Not Exist")
        return ptr
    


def insertionATSVA(ptr,data,sval):
    if ptr==None:
        newnode=Node(data)
        newnode.next=ptr
        newnode.prev=None
        ptr.prev=newnode
        return newnode     
    if ptr.data==sval:
        newnode=Node(data)
        newnode.next=ptr.next
        newnode.prev=ptr
        ptr.next.prev=newnode
        ptr.next=newnode
        return ptr
    flag=False
    copyptr=ptr
    while copyptr!=None:
        if copyptr.data==sval:
            flag=True
            break
        else:
            flag=False
        copyptr=copyptr.next
        
    if flag==True:
        qtr=ptr
        ftr=qtr.next
        
        while qtr.data!=sval:
            qtr=qtr.next
            ftr=ftr.next
        
        if ftr==None:
            newnode=Node(data)
            newnode.next=ftr
            newnode.prev=qtr
            qtr.next=newnode
            return ptr
        newnode=Node(data)
        newnode.next=ftr
        newnode.prev=qtr
        qtr.next=newnode
        ftr.prev=newnode
        return ptr
    else:
        print("Search Value Does Not Exist")
        return ptr


 
def deletionATB(ptr):
    if ptr==None:
        return None
    ptr=ptr.next
    ptr.prev=None
    return ptr  

def deletionATEND(ptr):
    if ptr==None:
        return None
    if ptr.next==None:
        ptr=ptr.next
        return ptr
        
    qtr=ptr
    ftr=qtr.next 
    while ftr.next!=None:
        ftr=ftr.next
        qtr=qtr.next
    
    qtr.next=ftr.next
    ftr=None
    return ptr

def deletionATBT(ptr,index):
    if ptr==None:
        return None
    if index==0:
        ptr=ptr.next
        ptr.prev=None
        return ptr
    
    count=0
    copyptr=ptr
    while copyptr!=None:
        count=count+1
        copyptr=copyptr.next
    
    if count>index:
        qtr=ptr
        ftr=qtr.next
        i=0
        while i<index-1:
            qtr=qtr.next
            ftr=ftr.next
            i=i+1
        if ftr.next==None:
            return deletionATEND(a)
        qtr.next=ftr.next
        ftr.next.prev=qtr
        
        return ptr
    else:
        print("Index Out Of The Range")
        return ptr
    
def deletionATSV(ptr,sval):
    if ptr==None:
        return None
    if ptr.data==sval:
        ptr=ptr.next
        ptr.prev=None
        return ptr
    flag=False
    copyptr=ptr
    while copyptr!=None:
        if copyptr.data==sval:
            flag=True
            break
        else:
            flag=False
        copyptr=copyptr.next
    if flag==True:
        qtr=ptr
        ftr=qtr.next
        while ftr.data!=sval:
            qtr=qtr.next
            ftr=ftr.next
        if ftr.next==None:
            qtr.next=ftr.next
            return ptr
        qtr.next=ftr.next
        ftr.next.prev=qtr
        return ptr
    else:
        print("Search Value Does Not Exist")
        return ptr


    

a=Node(10)
b=Node(20)
c=Node(30)
d=Node(40)

a.prev=None
a.next=b

b.prev=a
b.next=c

c.prev=b
c.next=d

d.prev=c
d.next=None

a=insertionATB(a,5)
a=insertionATEND(a,50)
a=insertionATBT(a,60,3)
a=insertionATSVB(a,100,40)
a=insertionATSVA(a,150,50)
a=deletionATB(a)
a=deletionATEND(a)
a=deletionATBT(a,4)
a=deletionATSV(a,50)
a=deletionATBT(a,4)
Traversal(a)

