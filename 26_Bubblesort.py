x=[92,95,112,2,-1,62]

for i in range(len(x)):
    for j in range(len(x)-1-i):
        if x[j]>x[j+1]:
            t=x[j]
            x[j]=x[j+1]
            x[j+1]=t
            
            
print(x)