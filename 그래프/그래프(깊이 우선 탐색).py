# class , function
class Graph():
    def __init__ (self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# variable
G1 = None
stack = []
visitedAry = [] # 방문한 정점

# main
G1 = Graph(4)
G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print(" ** 무방향 그래프 ** ")
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end = ' ')
    print()

current = 0 # 시작 정점
stack.append(current)
visitedAry.append(current)

while (len(stack) != 0):
    next = None
    for vertex in range(4):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:    # 방문한 적이 있는 정점이면 탈락
                pass
            else:   # 방문한 적이 없으면 다음 정점으로 지정
                next = vertex
                break
    print("current : ", current, "vertex : ", vertex, "stack : ", stack)
    if next != None:    # 다음에 방문할 정점이 있는 경우
        current = next
        stack.append(current)
        visitedAry.append(current)
        print("current : ", chr(ord('A')+current), "stack : ", stack)
    else:   # 다음에 방문할 정점이 없는 경우
        current = stack.pop()
        print("pop : ", chr(ord('A')+current), "stack : ", stack)
print("방문 순서 -->", end = ' ')
for i in visitedAry:
    print(chr(ord('A')+ i), end = ' ')

# 출력

 ** 무방향 그래프 ** 
0 0 1 1
0 0 1 0
1 1 0 1
1 0 1 0
current :  0 vertex :  2 stack :  [0]
current :  C stack :  [0, 2]
current :  2 vertex :  1 stack :  [0, 2]
current :  B stack :  [0, 2, 1]
current :  1 vertex :  3 stack :  [0, 2, 1]
pop :  B stack :  [0, 2]
current :  1 vertex :  3 stack :  [0, 2]
pop :  C stack :  [0]
current :  2 vertex :  3 stack :  [0]
current :  D stack :  [0, 3]
current :  3 vertex :  3 stack :  [0, 3]
pop :  D stack :  [0]
current :  3 vertex :  3 stack :  [0]
pop :  A stack :  []
방문 순서 --> A C B D