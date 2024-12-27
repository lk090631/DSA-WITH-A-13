class queue:
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
    newnode=queue(data)
    if newnode==None:
        return True
    else:
        return False
    

def enqueue(ptr,data):
    if isFull(ptr,data):
        print("Queue Is Full Now")
        return ptr
    else:
        if ptr==None:
            newnode=queue(data)
            newnode.next=None
            return newnode
        qtr=ptr
        while qtr.next!=None:
            qtr=qtr.next    
        newnode=queue(data)
        newnode.next=None
        qtr.next=newnode
        return ptr
    
def dequeue(ptr):
    if isEmpty(ptr):
        print("Queue Is Empty Now")
        return ptr
    else:
        if ptr==None:
            return None
        ptr=ptr.next
        return ptr


def peek(ptr):
    while ptr!=None:
        print(ptr.data)
        ptr=ptr.next

head=None

head=enqueue(head,10)
head=enqueue(head,20)
head=enqueue(head,30)
head=enqueue(head,40)
head=enqueue(head,50)

head=dequeue(head)
head=dequeue(head)
head=dequeue(head)
head=dequeue(head)
head=dequeue(head)
head=dequeue(head)
peek(head)