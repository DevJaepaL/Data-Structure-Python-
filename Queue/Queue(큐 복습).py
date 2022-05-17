# 큐(Queue)란?
# 기차가 터널에 들어가는 순서대로 터널을 빠져나오고,
# ATM기에서 줄을 선 순서대로 예금을 인출하는 것처럼,
# 큐는 먼저 들어간 것이 먼저 나오는 구조를 의미 (선입선출, 후입후출)

# 큐의 개념
# 큐(Queue) 자료구조는 입구와 출구가 따로 있는 형태

# 큐의 원리
#   구조와 용어
#       큐에 데이터를 삽입하는 작동 : enQueue(인큐)
#       큐에 데이터를 추출하는 작동 : deQueue(데큐)
#       저장된 데이터 중 첫번째 데이터 : front(머리) * head 라고도 함.
#       저장된 데이터 중 마지막 데이터 : rear(꼬리)

# 큐의 생성

queue = [None, None, None, None, None] # 크기가 5칸인 변수 queue 배열
front = rear = -1 # 기본값은 -1 이다.

# 데이터 삽입 : enQueue

rear += 1
queue[rear] = "101번 방"

rear += 1
queue[rear] = "102번 방"

rear += 1
queue[rear] = "103번 방"

print("[Exit] <==", end = ' ')
for i in range(0,len(queue),1):
    print(queue[i],end = ' ')
print("<== [Enter]")

# 출력 결과
[Exit] <== 101번 방 102번 방 103번 방 None None <== [Enter]

# 데이터 추출 : deQueue

queue = ["101번 방", "102번 방", "103번 방", None, None]
front = -1
rear = 2

print("==== 현재 큐 상태 ====")
print("[Exit] <== ", end = ' ')
for i in range(0,len(queue),1):
    print(queue[i], end = ' ')
print("<== [Enter]")
print("======================")

front += 1
data = queue[front]
queue[front] = None
print('deQueue ==>', data)

front += 1
data = queue[front]
queue[front] = None
print('deQueue ==>', data)

front += 1
data = queue[front]
queue[front] = None
print('deQueue ==>', data)

print("==== 현재 큐 상태 ====")
print("[Exit] <==",queue, end = " <== [Enter]")

# 실행 결과
==== 현재 큐 상태 ====
[Exit] <==  101번 방 102번 방 103번 방 None None <== [Enter]
======================
deQueue ==> 101번 방
deQueue ==> 102번 방
deQueue ==> 103번 방
==== 현재 큐 상태 ====
[Exit] <== [None, None, None, None, None] <== [Enter]


# 큐 초기화
# SIZE 값만 변경하면 원하는 크기의 빈 큐 생성 (초기화)

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

print(queue)

# 실행 결과

[None, None, None, None, None]

# 데이터 삽입 과정
  큐가 꽉 찼는지 확인하는 함수
  rear 값이 '큐의 크기 - 1'와 같다면 큐가 꽉찬 상태

def isQueueFull():
    global SIZE,queue,front,rear
    if (rear == SIZE-1):
        return True
    else:
        return False

SIZE = 4
queue = ["101호", "102호", "103호", "104호"]
front = -1
rear = 3

print("큐가 꽉 차있나요 ? : ", isQueueFull())

# 실행 결과 
큐가 꽉 차있나요 ? :  True


# 큐에 데이터를 삽입하는 함수

def enQueue(data):
    global SIZE,queue,front,rear
    if(rear == SIZE-1):
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

SIZE = 5
queue = ["101호", "102호", "103호", "104호", None]
front = -1
rear = 3

print(queue)
enQueue("105호")
print(queue)
enQueue("106호")

# 실행 결과
['101호', '102호', '103호', '104호', None]
['101호', '102호', '103호', '104호', '105호']
큐가 꽉 찼습니다.

# 큐가 비었는지 확인하는 함수
#   front와 rear의 값이 같다면 큐가 비어있는 상태
#   if (front == rear):

def isQueueEmpty():
    global SIZE,queue,front,rear
    if(front == rear):
        return True
    else:
        return False

SIZE = 3
queue = [None for _ in range(SIZE)]
front = rear = -1

# print("큐가 비어있나요 ? : ", isQueueEmpty())

# 실행 결과
큐가 비어있나요 ? :  True

# 큐에서 데이터를 추출하는 함수

def deQueue():
    global SIZE, queue, front, rear
    if (front == rear):
        print("큐가 비었어요.")
        return None

    front += 1
    data = queue[front]
    queue[front] = None
    return data

SIZE = 5
queue = ["101호", None, None, None, None]
front = -1
rear = 0

print(queue)
retData = deQueue()
print("추출한 데이터 =>", retData)
print(queue)
retData = deQueue()

# 실행 결과
['101호', None, None, None, None]
추출한 데이터 => 101호
[None, None, None, None, None]
큐가 비었어요.

# 데이터 확인 (peek)
#   추출될 데이터를 큐에 그대로 두고 확인만 하는 것

def peek():
    global SIZE,queue,front,rear
    if (front == rear):
        print("큐가 비었어요.")
        return None
    return queue[front+1]

SIZE = 5
queue = ["101호","102호","103호",None,None]
front = -1
rear = 2

print(queue)
retData = peek()
print("추출한 데이터 : ",retData)
print(queue)

# 실행 결과
['101호', '102호', '103호', None, None]
추출한 데이터 :  101호
['101호', '102호', '103호', None, None]


# 큐 완성하기.
# 함수 구현
def isQueueFull():
    global SIZE,queue,front,rear
    if(rear == SIZE-1):
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE,queue,front,rear
    if (front == rear):
        return True
    else:
        return False

def enQueue(data):
    global SIZE,queue,front,rear
    if(isQueueFull()):
        print("큐가 꽉찼어요.")
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print("큐가 비었어요.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print("큐가 비었어요.")
        return None
    return queue[front+1]

# 전역 변수 선언
SIZE = int(input("큐 크기를 입력 해주세요. : "))
queue = [None for _ in range(SIZE)]
front = rear = -1

# 메인 코드 구현

if __name__ == "__main__":
   select = input("[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : ")

    while(select != 'R' and select != 'R'):
        if select == 'Q' or select == 'q':
            data = input("데이터 입력 : ")
            enQueue(data)
            print("현재 큐의 형태 : ", queue)
        elif select == 'W' or select == 'w':
            data = deQueue()
            print("추출한 데이터 : ", data)
            print("현재 큐의 상태 : ", queue)
        elif select == 'E' or select == 'e':
            data = peek()
            print("확인된 데이터 : ", data)
            print("현재 큐의 상태 : ", queue)
        else:
            print("입력을 잘못했어요.")

        select = input("[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : ")

    print("프로그램 종료.")

# 실행 결과

큐 크기를 입력 해주세요. : 5
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : Q
데이터 입력 : 한국
현재 큐의 형태 :  ['한국', None, None, None, None]
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : Q
데이터 입력 : 일본
현재 큐의 형태 :  ['한국', '일본', None, None, None]
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : Q
데이터 입력 : 미국
현재 큐의 형태 :  ['한국', '일본', '미국', None, None]
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : W
추출한 데이터 :  한국
현재 큐의 상태 :  [None, '일본', '미국', None, None]
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : E
확인된 데이터 :  일본
현재 큐의 상태 :  [None, '일본', '미국', None, None]
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : W
추출한 데이터 :  일본
현재 큐의 상태 :  [None, None, '미국', None, None]
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : W
추출한 데이터 :  미국
현재 큐의 상태 :  [None, None, None, None, None]
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : E
큐가 비었어요.
확인된 데이터 :  None
현재 큐의 상태 :  [None, None, None, None, None]
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : R
프로그램 종료.

# 큐가 찼는지 확인하는 함수의 문제가 있어, 기능 개선이 필요함.
# 해결법
#   if (rear != SIZE -1) ==> 큐가 꽉 차지 않음.
#   elif (rear == SIZE -1) and (front == -1) ==> 큐가 꽉 참.
#   else ==>  데이터를 앞으로 당기면 큐가 꽉차지 않는다.
def isQueueFull():
    global SIZE,queue,front,rear
    if(rear != SIZE-1):
        return False
    elif(rear == SIZE-1) and (front == -1):
        return True
    else:
        for i in range(front+1,SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

# 원형 큐 : 큐의 처음과 끝이 연결된 구조
# 원형 큐 = [None, None, None, None, None]
# front = rear = 0

# 원형 큐가 빈 경우 :
#   if(front == rear) ==> 큐가 비었다.
# 원형 큐가 꽉 찬 경우 :
#   if((rear + 1)%5 == front)
# 원형 큐는 한칸을 비워두고 운영해야 합니다 !

# 원형 큐의 데이터 삽입
#   if(큐가 꽉 참.): ==> return
#   rear = (rear+1) % SIZE
#   queue[rear] = "화사"

# 원형 큐의 데이터 추출
#   if(큐가 비었음.) ==> return
#   front = (front+1) % SIZE
#   data = queue[front]
#  queue[front] = None

# 원형 큐 구현

# 함수 구현
def isQueueFull():
    global SIZE,queue,front,rear
    if((rear+1)%SIZE == front):
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE,queue,front,rear
    if(front == rear):
        return True
    else:
        return False

def enQueue(data):
    global SIZE,queue,front,rear
    if(isQueueFull()):
        print("큐가 꽉 찼어요.")
        return
    rear = (rear+1) % SIZE
    queue[rear] = data

def deQueue():
    global SIZE,queue,front,rear
    if(isQueueEmpty()):
        print("큐가 비었어요.")
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    if(isQueueEmpty()):
      print("큐가 비었어요.")
      return None
    return queue[(front+1)% SIZE]

# 전역 변수 선언
SIZE = int(input("큐 크기를 입력해주세요. : "))
queue = [None for _ in range(SIZE)]
front = rear = 0

# 메인 코드
if __name__ == "__main__":
    select = input("[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : ")
    while(select != 'R' and select != 'R'):
        if select == 'Q' or select == 'q':
            data = input("데이터 입력 : ")
            enQueue(data)
            print("현재 큐의 형태 : ", queue)
            print("front : ", front, "rear : ", rear)
        elif select == 'W' or select == 'w':
            data = deQueue()
            print("추출한 데이터 : ", data)
            print("현재 큐의 상태 : ", queue)
            print("front : ", front, "rear : ", rear)
        elif select == 'E' or select == 'e':
            data = peek()
            print("확인된 데이터 : ", data)
            print("현재 큐의 상태 : ", queue)
            print("front : ", front, "rear : ", rear)
        else:
            print("입력을 잘못했어요.")

        select = input("[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : ")

    print("프로그램 종료.")

# 실행 결과
큐 크기를 입력해주세요. : 4
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : Q
데이터 입력 : 한국
현재 큐의 형태 :  [None, '한국', None, None]
front :  0 rear :  1
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : Q
데이터 입력 : 중국
현재 큐의 형태 :  [None, '한국', '중국', None]
front :  0 rear :  2
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : Q
데이터 입력 : 일본
현재 큐의 형태 :  [None, '한국', '중국', '일본']
front :  0 rear :  3
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : E
확인된 데이터 :  한국
현재 큐의 상태 :  [None, '한국', '중국', '일본']
front :  0 rear :  3
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : Q
데이터 입력 : 미국
큐가 꽉 찼어요.
현재 큐의 형태 :  [None, '한국', '중국', '일본']
front :  0 rear :  3
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : W
추출한 데이터 :  한국
현재 큐의 상태 :  [None, None, '중국', '일본']
front :  1 rear :  3
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : W
추출한 데이터 :  중국
현재 큐의 상태 :  [None, None, None, '일본']
front :  2 rear :  3
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : W
추출한 데이터 :  일본
현재 큐의 상태 :  [None, None, None, None]
front :  3 rear :  3
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : Q
데이터 입력 : 한국
현재 큐의 형태 :  ['한국', None, None, None]
front :  3 rear :  0
[ 삽입(Q) | 추출(W) | 체크(E) | 종료(R) ] : R
프로그램 종료.    