import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
                
city, path, start = map(int,input().split())
graph = [[]for i in range(city + 1)]
distance = [INF] * (city + 1)

for _ in range(path):
    x, y, z = map(int,input().split())
    graph[x].append((y,z))

dijkstra(start)

cnt = 0
max_distance = 0

for i in distance:
    if i != 1e9:
        cnt += 1
        max_distance = max(max_distance,i)

print(cnt - 1, max_distance)
