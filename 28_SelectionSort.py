x=[77,44,22,39,86]

for i in range(len(x)):
    min_index=i
    for j in range(i+1,len(x)):
        if x[j]<x[min_index]:
            min_index=j
            
    t=x[i]
    x[i]=x[min_index]
    x[min_index]=t
        
print(x)