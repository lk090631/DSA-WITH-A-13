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
    newnode=Node(data)
    newnode.next=ptr
    return newnode


def insertionATEND(ptr,data):
    if ptr==None:
        newnode=Node(data)
        newnode.next=None
        return newnode
    qtr=ptr
    while qtr.next!=None:
        qtr=qtr.next    
    newnode=Node(data)
    newnode.next=None
    qtr.next=newnode
    return ptr

def RemoveDuplicates(ptr):
    
    arr=[]
    arrRemoveDuplicates=[]
    copyptr=ptr
    while copyptr!=None:
       arr.append(copyptr.data)
       copyptr=copyptr.next
       
    for i in range(len(arr)):
        if arr[i] not in arrRemoveDuplicates:
            arrRemoveDuplicates.append(arr[i])
    
    ptr=None
    for j in arrRemoveDuplicates:
        ptr=insertionATEND(ptr,j)
        
    return ptr


def insertionATBT(ptr,data,index):
    if ptr==None:
        newnode=Node(data)
        newnode.next=None
        return newnode
    if index==0:
        newnode=Node(data)
        newnode.next=None
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
        qtr.next=newnode
        return ptr
    else:
        print("Index Out Of The Range")
        return ptr
    

def insertionATSVB(ptr,data,sval):
    if ptr==None:
        newnode=Node(data)
        newnode.next=None
        return newnode
    if ptr.data==sval:
        newnode=Node(data)
        newnode.next=None
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
            ftr=ftr.next
            qtr=qtr.next
        newnode=Node(data)
        newnode.next=ftr
        qtr.next=newnode
        return ptr
    else:
        print("Search Value Does Not Exist")
        return ptr
    

  
def insertionATSVA(ptr,data,sval):
    if ptr==None:
        newnode=Node(data)
        newnode.next=None
        return newnode
    if ptr.data==sval:
        newnode=Node(data)
        newnode.next=ptr.next
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
            ftr=ftr.next
            qtr=qtr.next
        newnode=Node(data)
        newnode.next=ftr
        qtr.next=newnode
        return ptr
    else:
        print("Search Value Does Not Exist")
        return ptr
    


def deletionATB(ptr):
    if ptr==None:
        return None
    ptr=ptr.next
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
    return ptr
              
def deletionATBT(ptr,index):
    if ptr==None:
        return None
    if index==0:
        ptr=ptr.next
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
        
        qtr.next=ftr.next
        return ptr
    else:
        print("Index Out Of The Range")
        return ptr
 
 
def deletionATSV(ptr,sval):
    if ptr==None:
        return None
    if ptr.data==sval:
        ptr=ptr.next
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
        while  ftr.data!=sval:
            ftr=ftr.next
            qtr=qtr.next
        qtr.next=ftr.next
        return ptr
    else:
        print("Search Value Does not Exist")
        return ptr




a=Node(10)
b=Node(20)
c=Node(30)
d=Node(40)

a.next=b
b.next=c
c.next=d
d.next=None

a=insertionATEND(a,70)
a=insertionATEND(a,70)
a=insertionATEND(a,50)
a=insertionATEND(a,60)
a=insertionATEND(a,70)
a=insertionATEND(a,70)


a=RemoveDuplicates(a)
Traversal(a)