# 클래스 및 함수선언 파트
class Node():
    def __init__(self):
        self.data = None
        self.link = None

# 데이터 출력 상수선언 파트
def printNodes(start):
    current = start
    if current.link == None:
        return
    print(current.data,end=' ')
    while current.link != start :
        current = current.link
        print(current.data,end=' ')
    print()

# 데이터 검색 상수선언 파트
def findNode(findData):
    global memory,head,current,pre #지역변수를 전역변수로 바꿔줌.

    current = head
    if current.data == findData:
        return current
    while current.link != head:
        current = current.link
        if current.data == findData:
            return current
    return Node() # 빈 노드 반환

# 전역 변수 선언 부분
memory = []
head,current,pre = None,None,None
dataArray = ["다현","정연","쯔위","사나","지효"]

# 메인코드 부분
if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0] #첫번째 노드
    head = node #헤드노드 지정
    node.link = head
    memory.append(node)

    for data in dataArray[1:]: #첫번째 노드 이후의 노드삽입 반복분 실행
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)
# 기존의 있는 노드들 출력
    printNodes(head)

    fNode = findNode("다현")
    print(fNode.data)

    fNode = findNode("지효")
    print(fNode.data)

    fNode = findNode("아이유")
    print(fNode.data)