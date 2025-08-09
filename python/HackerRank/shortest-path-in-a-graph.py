#https://www.hackerrank.com/contests/classroomtech-coding-contest/challenges/shortest-path-in-a-graph

n,m,s,t=map(int,input().split())
graph=[]
for i in range(n+1):
    graph.append([])

for i in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((v, w))

dist=[float('inf')]*(n+1)
dist[s] = 0

visited=[False]*(n+1)

for j in range(n):
    min_d =float('inf')
    u=-1
    for i in range(1,n+1):
        if not visited[i] and dist[i]<min_d:
            min_d=dist[i]
            u=i

    if u==-1:
        break

    visited[u]=True

    for v,w in graph[u]:
        if dist[v]>dist[u]+w:
            dist[v]=dist[u]+w

if dist[t]==float('inf'):
    print(-1)
else:
    print(dist[t])
