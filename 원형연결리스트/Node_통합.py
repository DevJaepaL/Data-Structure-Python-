#클래스 선언
class Node():
    def __init__(self):
        self.data = None
        self.link = None

#데이터 출력
def printNodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()

#데이터 삽입
def insertNode(findData,insertData):
    global memory,head,current,pre

    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insertData
    current.link = node
    node.link = head

#데이터 삭제
def deleteNode(deleteData):
    global memory,head,current,pre
    if head.data == deleteData:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del(current)
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

#데이터 검색
def findNode(findData):
    global memory,head,current,pre
    current = head
    if current.data == findData:
        return current
    while current.link != head:
        current = current.link
        if current.data == findData:
            return current
    return Node()

#전역 변수
memory = []
head,current,pre = None,None,None
dataArray = ["김범수","나얼","박효신","이수","하현우"]

#메인 코드
if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)
# 리스트 전체 출력
    printNodes(head)

# 노드 삽입
    insertNode("김범수","윤종신")
    printNodes(head)

#노드 삭제
    deleteNode("이수")
    printNodes(head)

#노드 검색
    fNode = findNode("아이유")
    print(fNode.data)