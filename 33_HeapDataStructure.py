
def insert(arr,data):
    arr.append(data)
    current=len(arr)-1
    while current>0:
        parent=(current-1)//2
        if arr[current]>arr[parent]:
            t=arr[current]
            arr[current]=arr[parent]
            arr[parent]=t
            current=parent
        else:
            break

def heapify(arr,length,i):
    largest=i
    left=2*i+1
    right=2*i+2
    
    if left<length and arr[left]>arr[largest]:
        largest=left
    if right<length and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        t=arr[i]
        arr[i]=arr[largest]
        arr[largest]=t
        heapify(arr,length,largest)

def build_heap(arr):
    for i in range((len(arr)//2)-1,-1,-1):
        heapify(arr,len(arr),i)        
        


def deletion(arr,num):
    i=0
    while i<len(arr):
        if arr[i]==num:
            break
        i=i+1
        
    t=arr[i]
    arr[i]=arr[len(arr)-1]
    arr[len(arr)-1]=t
    arr.pop()
    
    for i in range((len(arr)//2)-1,-1,-1):
        heapify(arr,len(arr),i)  
        
    



arr=[73,10,3,5,30,54,19,49,50,98]

build_heap(arr)


print(arr)
deletion(arr,54)
print(arr)