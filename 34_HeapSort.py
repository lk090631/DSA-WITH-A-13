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
        
        
def heap_sort(arr):
    new_arr=[]
    for i in range((len(arr)//2)-1,-1,-1):
        heapify(arr,len(arr),i) 
        
    for i in range(len(arr)):
        t=arr[0]
        arr[0]=arr[len(arr)-1]
        arr[len(arr)-1]=t
        new_arr.insert(0,arr.pop())
        heapify(arr,len(arr)-1,0)
    return new_arr
        
        
arr=[73,10,3,5,30,54,19,49,50,98]

arr=heap_sort(arr)
print(arr)