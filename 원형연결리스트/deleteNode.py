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

# 데이터 삭제 상수선언 파트
def deleteNode(deleteData):
    global memory,head,current,pre #지역변수를 전역변수로 바꿔줌.

    if head.data == deleteData :  #첫번째 노드 삭제 부분
        current = head
        head = head.link
        last = head
        while last.link != current: #마지막 노드를 찾으면 반복문 종료
            last = last.link #last를 다음 노드로 변경
        last.link = head #마지막 노드의 링크에 head가 가르키는 노드로 지정
        del(current)
        return
    
    current = head #첫번째 외 노드 삭제
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deleteData: #중간 노드의 값을 찾았을 경우
            pre.link = current.link
            del(current)
            return

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
# 노드 삭제
    deleteNode("다현")
    printNodes(head)

    deleteNode("정연")
    printNodes(head)    