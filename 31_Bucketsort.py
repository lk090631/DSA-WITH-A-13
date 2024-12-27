
def bucket_sort(arr):
    if len(arr)==0:
        return arr
    
    minvalue=min(arr)
    maxvalue=max(arr)
    size=len(arr)
    
    buckets=[[] for i in range(len(arr))]
    bucketrange=(maxvalue-minvalue+1)
    for i in range(len(arr)):
        elementrange=int((arr[i]-minvalue)/bucketrange*size)
        buckets[elementrange].append(arr[i])
       
    for j in range(len(arr)):
        buckets[j].sort()
        
    sorted=[]
    
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            sorted.append(buckets[i][j])
            
    print(sorted)
    

arr=[4,2,6,3,8,7,10,14]

bucket_sort(arr)