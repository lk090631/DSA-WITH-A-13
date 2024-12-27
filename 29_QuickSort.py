def quick_sort(arr):
    if len(arr)==0 or len(arr)==1:
        return arr
    
    pivot=arr[0]
    left=[]
    right=[]
    for i in range(1,len(arr)):
        if arr[i]<pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
            
            
    sorted_left=quick_sort(left)
    sorted_right=quick_sort(right)
    return [*sorted_left,pivot,*sorted_right]


arr=[8,7,6,1,0,9,8,20,20,5,10]
print(quick_sort(arr))