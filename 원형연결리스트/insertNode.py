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

# 첫번째 데이터 삽입하는 상수선언 파트
def insertNode(findData, insertData):
    global memory,head,current,pre #지역변수를 전역변수로 바꿔줌.
    if head.data == findData: #첫번째 노드 삽입
        node = Node()
        node.data = insertData
        node.link = head
        last = head #마지막 노드를 첫번째 노드로 우선 지정
        while last.link != head: #마지막 노드를 헤드까지 반복문 실행
            last = last.link #마지막 노드를 찾으면 반복문 종료
        last.link = node #마지막 노드의 링크에 새 노드 지정
        head = node
        return
    current = head # 중간 데이터 삽입부분
    while current.link != head:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
# 마지막 데이터 삽입부분
    node = Node()
    node.data = insertData
    current.link = node
    node.link = head

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
# 다현 노드의 앞에 화사 노드 삽입
    insertNode("다현","화사")
    printNodes(head)

    insertNode("사나","솔라")
    printNodes(head)

    insertNode("재남","문별")
    printNodes(head)