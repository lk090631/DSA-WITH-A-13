class stack:
    arr=[None]
    size=None
    top1=None
    top2=None


def isEmptyT1(ptr):
    if ptr.top1==-1:
        return True
    else:
        return False

def isEmptyT2(ptr):
    if ptr.top2==ptr.size:
        return True
    else:
        return False
    
def isFull(ptr):
    if ptr.top1+1==ptr.top2:
        return True
    else:
        return False
    

def push1(ptr,data):
    if isFull(ptr):
        print("Stack Is Full Now")
        return ptr
    else:
        ptr.top1=ptr.top1+1
        ptr.arr[ptr.top1]=data
        return ptr
    
def push2(ptr,data):
    if isFull(ptr):
        print("Stack Is Full Now")
        return ptr
    else:
        ptr.top2=ptr.top2-1
        ptr.arr[ptr.top2]=data
        return ptr
 

def pop1(ptr):
    if isEmptyT1(ptr):
        print("Stack Is Empty Now")
        return ptr
    else:
        ptr.arr[ptr.top1]=None
        ptr.top1=ptr.top1-1
        return ptr
    
def pop2(ptr):
    if isEmptyT2(ptr):
        print("Stack Is Empty Now")
        return ptr
    else:
        ptr.arr[ptr.top2]=None
        ptr.top2=ptr.top2+1
        return ptr

    
def peek1(ptr):
    for i in range(ptr.top1,-1,-1):
        print(ptr.arr[i])
        
def peek2(ptr):
    for i in range(ptr.top2,ptr.size,1):
        print(ptr.arr[i])
    
           
    
        

head=stack()
head.size=10
head.top1=-1
head.top2=head.size
head.arr=head.arr*head.size

head=push1(head,10)
head=push1(head,20)
head=push1(head,30)
head=push1(head,40)
head=push1(head,50)
head=push1(head,60)

head=push2(head,70)
head=push2(head,80)
head=push2(head,90)
head=push2(head,100)




print("From Beginning")
peek1(head)
print("From End")
peek2(head)