distance_matrix=[
    [0,3,0,8,7],
    [3,0,1,4,0],
    [0,1,0,2,0],
    [8,4,2,0,3],
    [7,0,0,3,0]
]


def dijkstra(distance_matrix,start):
    distances=[float("inf")]*len(distance_matrix)
    visited=[0]*len(distance_matrix)
    distances[start]=0
    
    for i in range(len(distance_matrix)):
        min_distance=float("inf")
        min_node=None
        for j in range(len(distance_matrix)):
            if not visited[j] and distances[j]<min_distance:
                min_distance=distances[j]
                min_node=j        
        
        visited[min_node]=1
        
        for k in range(len(distance_matrix)):
            if distance_matrix[min_node][k]>0:
                newdistance=distances[min_node]+distance_matrix[min_node][k]
                if newdistance<distances[k]:
                    distances[k]=newdistance
                    
    return distances
    
    
    
ditance=dijkstra(distance_matrix,0)

print(ditance)