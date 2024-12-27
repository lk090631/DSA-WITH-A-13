class queue:
    arr=None
    size=None
    
    
def isEmpty(ptr):
    if len(ptr.arr)==0:
        return True
    else:
        return False
    
def isFull(ptr):
    if len(ptr.arr)==ptr.size:
        return True
    else:
        return False
    
def enqueueB(ptr,data):
    if isFull(ptr):
        print("Queue Is Full Now")
        return ptr
    else:
        ptr.arr.insert(0,data)
        return ptr
    
def enqueueEnd(ptr,data):
    if isFull(ptr):
        print("Queue Is Full Now")
        return ptr
    else:
        ptr.arr.append(data)
        return ptr
    
def dequeueB(ptr):
    if isEmpty(ptr):
        print("Queue Is Empty Now")
        return ptr
    else:
        del ptr.arr[0]
        return ptr
    
def dequeueEnd(ptr):
    if isEmpty(ptr):
        print("Queue Is Empty Now")
        return ptr
    else:
        ptr.arr.pop()
        return ptr
    
    
head=queue()
head.arr=[]
head.size=10

head=enqueueB(head,10)
head=enqueueB(head,20)
head=enqueueB(head,30)

head=enqueueEnd(head,40)
head=enqueueEnd(head,50)
head=enqueueB(head,70)
head=enqueueB(head,80)
head=enqueueB(head,90)
head=enqueueB(head,100)
head=enqueueB(head,110)

head=dequeueB(head)
head=dequeueB(head)
head=dequeueEnd(head)
head=dequeueEnd(head)
head=dequeueEnd(head)
head=dequeueEnd(head)
head=dequeueEnd(head)
head=dequeueEnd(head)
head=dequeueEnd(head)
head=dequeueEnd(head)
head=dequeueEnd(head)
head=dequeueEnd(head)
print(head.arr)
    
    
