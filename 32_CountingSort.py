def counting_sort(arr):
    if len(arr)==0:
        return arr
    
    count=[0]*(max(arr)+1)
    for i in range(len(arr)):
        count[arr[i]]+=1
     
    sorted_arr=[]    
    for i in range(len(count)):
        if count[i]>0:
            for j in range(count[i]):
                sorted_arr.append(i)
                
                
    print(sorted_arr)

        
    
        
    
    
    
    
    
    
arr=[11,5,2,12,9,9,3,2]
counting_sort(arr)