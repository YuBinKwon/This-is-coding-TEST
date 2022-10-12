# 탐색 알고리즘 DFS/BFS

# DFS : Depth-First Search. 깊이 우선 탐색 (깊은 노드부터 탐색)
# 노드+간선
# 스택을 이용하는 알고리즘이므로 재귀 함수를 이용
# 1) 탐색 시작 노드를 스택에 삽입하고 방문 처리.
# 2) 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문처리.
#    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3) 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.


# 1. 인접 행렬 방식 : 2차원 배열에 각 노드가 연결된 형태 기록

inf = 999999999 #무한의 비용 선언

graph = [
    [0,7,5],
    [7,0,inf],
    [5,inf,0]
]

print(graph)

# 2. 인접 리스트 방식 : 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결해 저장

graph = [[] for _ in range(3)]
# 노드 0에 연결된 노드 정보 저장 (노드,거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장 (노드,거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장 (노드,거리)
graph[2].append((0,5))

print(graph)


# DFS 예제

def dfs(graph,v,visited):
    #현재노드 방문처리
    visited[v]=True
    print(v,end=' ')
    #현재노드와 연결된 다른노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph=[ #리스트 자료형
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
dfs(graph,1,visited) # 1-2-7-6-8-3-4-5


# BFS : Breadth First Search. 너비 우선 탐색 (가까운 노드부터 탐색)
# 선입선출 큐 자료구조 이용
# 1) 탐색 시작 노드를 큐에 삽입하고 방문처리.
# 2) 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리.
# 3) 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.


# BFS 예제

from collections import deque

def bfs(graph,start,visited):
    #큐 구현을 위해 deque 라이브러리 사용
    queue=deque([start])
    visited[start]=True

    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나씩 원소를 뽑아 출력
        v=queue.popleft()
        print(v,end=' ')
        #해당 원소와 연결된, 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
bfs(graph,1,visited) # 1-2-3-8-7-4-5-6
