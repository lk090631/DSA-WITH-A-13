matrix=[
    [0,1,1,0,0,0],
    [1,0,0,1,1,0],
    [1,0,0,0,1,0],
    [0,1,0,0,0,1],
    [0,1,1,0,0,1],
    [0,0,0,1,1,0]
]

visited=[0,0,0,0,0,0]


def dfs(pos):
    print(pos)
    visited[pos]=1
    for i in range(len(visited)):
        if matrix[pos][i]==1 and visited[i]==0:
            dfs(i)
            

def Add_vertex():
    global matrix,visited
    for i in range(len(matrix)):
        matrix[i].append(0)
    matrix.append([0]*(len(matrix)+1))
    visited.append(0)
    
def Add_Edges(v1,v2):
    global matrix
    if v1< len(matrix) and v2< len(matrix):
        matrix[v1][v2]=1
        matrix[v2][v1]=1
    else:
        print("Both Vertex One Or Vertex 2 Does\'t Exist")
        
def Delete_Vertex():
    global matrix,visited
    matrix.pop()
    for i in range(len(matrix)):
        matrix[i].pop()
        
    visited.pop()
    
def Delete_Edges(v1,v2):
    global matrix
    if v1< len(matrix) and v2< len(matrix):
        matrix[v1][v2]=0
        matrix[v2][v1]=0
    else:
        print("Both Vertex One Or Vertex 2 Does\'t Exist")
            


Add_vertex()
Add_Edges(2,6)
Add_vertex()
Add_Edges(3,7)


# print(matrix)
dfs(0)



    