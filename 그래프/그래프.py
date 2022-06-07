# 그래프 구조
#   버스 정류장 , 지하철 노선도와 같이 여러 노드가 연결된 자료 구조
#   그래프의 종류에는 여러가지가 있음.
#   아래의 그래프는 무방향 그래프이며, 간선에 방향성이 없다.


# 기본적인 그래프의 정점 생성.
#   행과 열이 같은 2차원 배열을 생성하는 클래스로 작성
# function , class part
class Graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# variable part
G1 = None

# # main
G1 = Graph(4) # 4x4 크기의 배열 생성
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print("** G1(4x4)-무방향 그래프 **")
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end=' ')
    print()

출력
** G1(4x4)-무방향 그래프 ** 
0 1 1 1 
1 0 1 0 
1 1 0 1 
1 0 1 0 

# 무방향 그래프를 인접 행렬로 구성시 가독성을 위해 
# 사람의 이름이나 도시 이름으로 구성을 해보았다.

# function , class part
class Graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    print('     ', end = '      ')
    for v in range(g.SIZE):
        print(nameAry[v], end='   ')
    print()
    for row in range(g.SIZE):
        print(nameAry[row], end= '      ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end='      ')
        print()
    print()

# variable part
G1 = None
nameAry = ['흥민', '케인', '쿨루', '호이', '벤탄', '로메']
Son,Kane,Kulu,Hoj,Bent,Rome = 0,1,2,3,4,5

# main
gSize = 6
G1 = Graph(gSize)
G1.graph[Son][Kane] = 1; G1.graph[Son][Kulu] = 1
G1.graph[Kane][Son] = 1; G1.graph[Kane][Hoj] = 1
G1.graph[Kulu][Son] = 1; G1.graph[Kulu][Hoj] = 1
G1.graph[Hoj][Kane]= 1; G1.graph[Hoj][Kulu] = 1; 
G1.graph[Hoj][Bent] = 1; G1.graph[Hoj][Rome] = 1
G1.graph[Bent][Hoj] = 1; G1.graph[Bent][Rome] = 1
G1.graph[Rome][Hoj] = 1; G1.graph[Rome][Bent] = 1

print("     **   Variable G1 무방향 그래프   **     ")
printGraph(G1)

# 출력
     **   Variable G1 무방향 그래프   **     
         흥민   케인   쿨루   호이   벤탄   로메
흥민      0      1      1      0      0     0
케인      1      0      0      1      0     0
쿨루      1      0      0      1      0     0
호이      0      1      1      0      1     1
벤탄      0      0      0      1      0     1
로메      0      0      0      1      1     0