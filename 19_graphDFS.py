matrix=[
    [0,0,1,1],
    [0,0,1,1],
    [1,1,0,1],
    [1,1,1,0]
]

visited=[0,0,0,0]

def dfs(pos):
    print(pos)
    visited[pos]=1
    for i in range(len(visited)):
        if matrix[pos][i]==1 and visited[i]==0:
            dfs(i)
            
            
dfs(3)
    