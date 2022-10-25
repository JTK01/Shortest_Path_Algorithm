INF = 1e9

N, M = map(int,input().split())
graph = [[INF]*(N + 1) for _ in range(N + 1)]
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0
for i in range(M):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

X, K = map(int,input().split())
for i in range(1,N + 1):
    for j in range(1,N + 1):
        for k in range(1,N + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
distance = graph[1][K] + graph[K][X]

if distance >= INF:
    print("-1")
else:
    print(distance)
