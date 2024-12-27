
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
        
        

arr=[]
insert(arr,10)
insert(arr,55)
insert(arr,32)
insert(arr,45)
insert(arr,25)
insert(arr,16)
insert(arr,88)
insert(arr,99)
print(arr)