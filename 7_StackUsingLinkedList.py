class stack:
    data=None
    next=None
    def __init__(self,data):
        self.data=data
        


def isEmpty(ptr):
    if ptr==None:
        return True
    else:
        return False
    
def isFull(ptr,data):
    newnode=stack(data)
    if newnode==None:
        return True
    else:
        return False
    
def push(ptr,data):
    if isFull(ptr,data):
        print("Stack Is Full Now")
        return ptr
    else:
        if ptr==None:
            newnode=stack(data)
            newnode.next=None
            return newnode
        qtr=ptr
        while qtr.next!=None:
            qtr=qtr.next    
        newnode=stack(data)
        newnode.next=None
        qtr.next=newnode
        return ptr
    
def peek(ptr):
    arr=[]
    while ptr!=None:
        arr.append(ptr.data)
        ptr=ptr.next
    arr.reverse()
    print(*arr)
    
def pop(ptr):
    if isEmpty(ptr):
        print("Stack Is Empty Now")
        return ptr
    else:
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
    

    
head=None

head=push(head,10)
head=push(head,20)
head=push(head,30)
head=push(head,40)
head=push(head,50)
head=push(head,60)
head=pop(head)
head=pop(head)
head=pop(head)
head=pop(head)
head=pop(head)
head=pop(head)
head=pop(head)

peek(head)