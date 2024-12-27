
x=[77,86,65,4,33]

for i in range(1,len(x)):
    value=x[i]
    j=i-1
    while j>=0 and value<x[j]:
        x[j+1]=x[j]
        j=j-1
         
    x[j+1]=value
    
    
print(x)