def prism_algorith(matrix,vertices):
    inf=float("inf")
    visited=[0]*vertices
    visited[0]=1
    totalcost=0
    for i in range(vertices-1):
        min_weight=float("inf")
        x=0
        y=0
        for j in range(vertices):
            if visited[j]:
                for k in range(vertices):
                    if visited[k]==0 and matrix[j][k]!=0 and matrix[j][k]<min_weight:
                        min_weight=matrix[j][k]
                        x=j
                        y=k
        print("Edge",x,y)
        totalcost+=matrix[x][y]
        visited[y]=1
    print("Total Cost Of MST is",totalcost)
    
    
    
cost_matrix=[
    [0,2,0,4,0],
    [2,0,3,7,0],
    [0,3,0,0,3],
    [4,7,0,0,4],
    [0,0,3,4,0]
]

prism_algorith(cost_matrix,5)
        