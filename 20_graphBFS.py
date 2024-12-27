class queue:
    arr=[None]
    size=None
    front=None
    rear=None

def isEmpty(ptr):
    if ptr.rear==ptr.front:
        return True
    else:
        return False
    
def isFull(ptr):
    if ptr.rear==ptr.size-1:
        return True
    else:
        return False
    
def enqueue(ptr,data):
    if isFull(ptr):
        print("Queue Is Already Full")
        return ptr
    else:
        ptr.rear=ptr.rear+1
        ptr.arr[ptr.rear]=data
        return ptr
    
def dequeue(ptr):
    if isEmpty(ptr):
        print("Queue Is Empty Now")
        return ptr
    else:
        ptr.front=ptr.front+1
        temp=ptr.arr[ptr.front]
        ptr.arr[ptr.front]=None
        return temp
    
head=queue()
head.size=10
head.front=-1
head.rear=-1
head.arr=head.arr*head.size


matrix=[
    [0,0,1,1],
    [0,0,1,1],
    [1,1,0,1],
    [1,1,1,0]
]

visited=[0,0,0,0]

pos=1
print(pos)
visited[pos]=1

head=enqueue(head,1)

while not isEmpty(head):
    uv=dequeue(head)
    for i in range(len(visited)):
        if matrix[uv][i]==1 and visited[i]==0:
            print(i)
            visited[i]=1
            head=enqueue(head,i)