def dijkstra_algorithm(n,matrix,dist,visited):
    for i in range(n):
        u=None
        min_dis=float("inf")
        for j in range(n):
            if dist[j]<min_dis and visited[j]==False:
                u=j
                min_dis=dist[j]
        if u==None:
            break
        visited[u]=True
        for v in range(n):
            if matrix[u][v]!=0 and visited[v]==False:
                distance=matrix[u][v]+dist[u]
                if distance<dist[v]:
                    dist[v]=distance
matrix=[[0,6,0,0,8,7],[6,0,9,0,0,0],[0,9,0,12,0,0],[0,0,12,0,3,5],[8,0,0,3,0,10],[7,0,0,5,10,0]]
n=len(matrix)
dist=[float("inf")]*n
vertices=['A','B','C','D','E','F']
dist[0]=0
visited=[False]*n
dijkstra_algorithm(n,matrix,dist,visited)

print(f"Shortest Distances from Source Node to every other nodes are\n")
for i in range(1,len(vertices)):
    print(f"A-{vertices[i]} is {dist[i]}\n")