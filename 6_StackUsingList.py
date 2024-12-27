class stack:
    arr=[None]
    top=None
    size=None
    
 
def isEmpty(ptr):
    if ptr.top==-1:
        return True
    else:
        return False 
    
def isFull(ptr):
    if ptr.top==ptr.size-1:
        return True
    else:
        return False

def push(ptr,data):
    if isFull(ptr):
        print("Stack Is Full Now")
        return ptr
    else:
        ptr.top=ptr.top+1
        ptr.arr[ptr.top]=data
        return ptr  

def pop(ptr):
    if isEmpty(ptr):
        print("Stack Is Already Empty")
        return ptr
    else:
        ptr.arr[ptr.top]=None
        ptr.top=ptr.top-1
        return ptr
 
def stacktop(ptr):
    if isEmpty(ptr):
        print("No Item Found in Stack")
    else:
        return ptr.arr[ptr.top]

def stackbottom(ptr):
    if isEmpty(ptr):
        print("No Item Found in Stack")
    else:
        return ptr.arr[0] 

def peek(ptr):
    for i in range(ptr.top,-1,-1):
        print(ptr.arr[i])

head=stack()
head.size=10
head.top=-1
head.arr=head.arr*head.size

head=push(head,10)
head=push(head,20)
head=push(head,30)
head=push(head,40)
head=push(head,50)
head=push(head,60)
head=push(head,70)
head=push(head,80)
head=push(head,90)
head=push(head,100)

head=pop(head)
head=pop(head)
head=pop(head)
head=pop(head)
head=pop(head)
head=pop(head)
head=pop(head)
head=pop(head)
head=pop(head)
head=pop(head)



head=push(head,10)
head=push(head,20)
head=push(head,30)
head=push(head,40)
head=push(head,50)
head=push(head,60)
head=push(head,70)
head=push(head,80)
head=push(head,90)
head=push(head,100)


print(stacktop(head))
print(stackbottom(head))
