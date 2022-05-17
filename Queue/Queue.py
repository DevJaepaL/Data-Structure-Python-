# 큐(Queue) 자료구조는 입구와 출구가 따로 있는 형태이다.
# 스택(Stack) 자료구조와는 달리, 선입선출 , 후입후출 형태이다.

# 큐의 생성
queue = [None, None, None, None , None]
front = rear = -1 # front(head)와 rear(tail)의 초기값 -1


# 큐의 데이터 삽입 (크기가 5칸인 큐의 생성 및 데이터 3개 삽입)
queue = [None, None, None, None, None]
front = rear = -1

rear += 1
queue[rear] = "화사"

rear += 1
queue[rear] = "솔라"

rear += 1
queue[rear] = "문별"

print("----- 큐 -----")
print('[출구] <==', end =' ')
for i in range(0,len(queue),1):
    print(queue[i],end=' ')
print('<==[입구]')

# 출력 시
# [출구] <== 화사 솔라 문별 None None <==[입구] #


# 데이터 추출 (deQueue)
queue = ["화사","솔라","문별","None","None"]
front = -1
rear = 2

print("----- 큐 -----")
print('[출구] <== ', end = ' ')
for i in range(0,len(queue),1):
    print(queue[i],end=' ')
print('<== [입구]')
print("--------------")

front += 1
data = queue[front]
queue[front] = None
print('deQueue -- >', data)

front += 1
data = queue[front]
queue[front] = None
print('deQueue -- >', data)

front += 1
data = queue[front]
queue[front] = None
print('deQueue -- >', data)
print("----------------")

print("----- 큐 -----")
print('[출구] <== ', end = ' ')
for i in range(0,len(queue),1):
    print(queue[i],end=' ')
print('<== [입구]')
print("--------------")

# 출력 시
# ----- 큐 ----- #
# [출구] <==  화사 솔라 문별 None None <== [입구] #
# --------------
# deQueue -- > 화사 #
# deQueue -- > 솔라 #
# deQueue -- > 문별 #
# ---------------- #
# ----- 큐 ----- #
# [출구] <==  None None None None None <== [입구] #
# -------------- #


# 큐의 초기화 (SIZE 값만 변경하면 원하는 크기의 빈 큐 생성)
SIZE = 5 # 큐 크기
queue = [None for _ in range(SIZE)]
front = rear = -1


# 큐가 꽉 찼는지 확인하는 함수
# rear(tail) 값이 '큐 크기 - 1' 와 같다면 큐가 꽉 찬 상태
def isQueueFull():
    global SIZE,queue,front,rear
    if(rear == SIZE-1):
        return True
    else:
        return False

SIZE = 5
queue = ["화사","솔라","문별","휘인","선미"]
front = -1
rear = 4

print("큐가 꽉 찼는지 여부 ==>", isQueueFull())

# 출력 시
# 큐가 꽉 찼는지 여부 ==> True #


# 큐에 데이터를 삽입하는 함수
def isQueueFull():
    global SIZE,queue,front,rear
    if(rear == SIZE-1):
        return True
    else:
        return False

def enQueue(data):
    global SIZE,queue,front,rear
    if (isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

SIZE = 5
queue = ["화사","솔라","문별","휘인",None]
front = -1
rear = 3

print(queue)
enQueue("선미")
print(queue)
enQueue("재남")

# 출력 시
# ['화사', '솔라', '문별', '휘인', None] #
# ['화사', '솔라', '문별', '휘인', '선미'] #
# 큐가 꽉 찼습니다. #


# 큐가 비었는지 확인하는 함수
# (front와 rear의 값이 같으면 큐가 비어있는 상태)
def isQueueEmpty():
    global SIZE,queue,front,rear
    if (front == rear):
        return True
    else:
        return False

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

print("큐가 비어있는지 ? ==> ", isQueueEmpty())

# 출력 시
# 큐가 비어있는지 ? ==>  True #


# 큐에서 데이터를 추출하는 함수
def isQueueEmpty():
    global SIZE,queue,front,rear
    if (front == rear):
        return True
    else:
        return False

def deQueue():
    global SIZE,queue,front,rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

SIZE = 5
queue = ["화사", None, None, None, None]
front = -1
rear = 0

print(queue)
retData = deQueue()
print("추출한 데이터 ==> ", retData)
print(queue)
redData = deQueue()

# 출력 시
# ['화사', None, None, None, None] #
# 추출한 데이터 ==>  화사 #
# [None, None, None, None, None] #
# 큐가 비었습니다. #


# 데이터 확인 (peek)
def isQueueEmpty():
    global SIZE,queue,front,rear
    if (front == rear):
        return True
    else:
        return False

def peek():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    return queue[front+1]

SIZE = 5
queue = ["화사","솔라","문별",None,None]
front = -1
rear = 2

print(queue)
retData = peek()
print("다음에 추출될 데이터 확인 ==> ", retData)
print(queue)

# 출력 시
# ['화사', '솔라', '문별', None, None] #
# 다음에 추출될 데이터 확인 ==>  화사 #
# ['화사', '솔라', '문별', None, None] #


# 큐의 완성 (통합 Code)

# ## 함수 선언 ##
def isQueueFull(): # 큐의 데이터가 차있는지 확인하는 함수
    global SIZE,queue,front,rear
    if (rear != SIZE - 1):
        return False
    elif (rear == SIZE - 1) and (front == -1):
        return True
    else:
        for i in range(front+1,SIZE):
            queue[i-1]=queue[i]
            queue[i]= None
        front -= 1
        rear -= 1
        return False

def isQueueEmpty(): # 큐가 비었는지 확인하는 함수
    global SIZE,queue,front,rear
    if (front == rear):
        return True
    else:
        return False

def EnQueue(data):
    global SIZE,queue,front,rear
    if(isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE,queue,front,rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    return queue[front+1]

# ## 전역 변수 선언 ##
SIZE = int(input("큐의 크기를 입력하세요. : "))
queue = [None for _ in range(SIZE)]
front = rear = -1

# ## 메인 코드 ##
if __name__ == "__main__":
    select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : ")

    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 : ")
            EnQueue(data)
            print("큐 상태 :" , queue)
        elif select == "E" or select == 'e':
            data = deQueue()
            print("추출한 데이터 : ", data)
            print("큐 상태 : ", queue)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인 된 데이터 : ", data)
            print("큐 상태 : ", queue)
        else:
            print("입력이 잘못 됬습니다.")

        select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : ")

    print("프로그램을 종료 합니다.")

# 출력 시 
# 큐의 크기를 입력하세요. : 5 #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : i #
# 입력할 데이터 : 치킨 #
# 큐 상태 : ['치킨', None, None, None, None] #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : i #
# 입력할 데이터 : 피자 #
# 큐 상태 : ['치킨', '피자', None, None, None] #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : i #
# 입력할 데이터 : 햄버거 #
# 큐 상태 : ['치킨', '피자', '햄버거', None, None] #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : e #
# 추출한 데이터 :  치킨 #
# 큐 상태 :  [None, '피자', '햄버거', None, None] #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : e #
# 추출한 데이터 :  피자 #
# 큐 상태 :  [None, None, '햄버거', None, None] #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : e #
# 추출한 데이터 :  햄버거 #
# 큐 상태 :  [None, None, None, None, None] #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : v #
# 큐가 비었습니다. #
# 확인 된 데이터 :  None #
# 큐 상태 :  [None, None, None, None, None] #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : x #
# 프로그램을 종료 합니다. #

# 원형 큐의 개념 : 큐의 처음과 끝이 연결 된 구조
# 원형 큐의 초기화
# 원형 큐 = [None, None, None, None, None]
# front = rear = 0


# 원형 큐 구현
## 함수 선언 ##
def isQueueFull(): # 큐의 데이터가 차있는지 확인하는 함수
    global SIZE,queue,front,rear
    if ((rear+1) % SIZE == front):
        return True
    else:
        return False

def isQueueEmpty(): # 큐가 비었는지 확인하는 함수
    global SIZE,queue,front,rear
    if (front == rear):
        return True
    else:
        return False

def EnQueue(data):
    global SIZE,queue,front,rear
    if(isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear+1)%SIZE
    queue[rear] = data

def deQueue():
    global SIZE,queue,front,rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front = (front+1)%SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    return queue[(front+1)%SIZE]

## 전역 변수 선언 ##
SIZE = int(input("큐의 크기를 입력하세요. : "))
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인 코드 ##
if __name__ == "__main__":
    select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : ")

    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 : ")
            EnQueue(data)
            print("큐 상태 :" , queue)
            print("front : ",front, "rear : ",rear)
        elif select == "E" or select == 'e':
            data = deQueue()
            print("추출한 데이터 : ", data)
            print("큐 상태 : ", queue)
            print("front : ",front, "rear : ",rear)
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인 된 데이터 : ", data)
            print("큐 상태 : ", queue)
            print("front : ",front, "rear : ",rear)
        else:
            print("입력이 잘못 됬습니다.")

        select = input("삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : ")

    print("프로그램을 종료 합니다.")

# 출력 시
# 큐의 크기를 입력하세요. : 5 #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : I #
# 입력할 데이터 : 치킨 #
# 큐 상태 : [None, '치킨', None, None, None] #
# front :  0 rear :  1 #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : I #
# 입력할 데이터 : 피자 #
# 큐 상태 : [None, '치킨', '피자', None, None] #
# front :  0 rear :  2 #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : I #
# 입력할 데이터 : 햄버거 #
# 큐 상태 : [None, '치킨', '피자', '햄버거', None] #
# front :  0 rear :  3 #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : E #
# 추출한 데이터 :  치킨 #
# 큐 상태 :  [None, None, '피자', '햄버거', None] #
# front :  1 rear :  3 #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : E #
# 추출한 데이터 :  피자 #
# 큐 상태 :  [None, None, None, '햄버거', None] #
# front :  2 rear :  3 #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : E #
# 추출한 데이터 :  햄버거 #
# 큐 상태 :  [None, None, None, None, None] #
# front :  3 rear :  3 #
# 삽입(I) / 추출(E) / 확인(V) / 종료(X) / 중 하나를 선택 : x #
# 프로그램을 종료 합니다. #