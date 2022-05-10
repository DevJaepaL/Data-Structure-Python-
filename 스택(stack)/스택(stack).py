# 스택의 개념
# 스택 자료구조는 한쪽 끝이 막힌 형태
# 입구가 하나이기 때문에  
# 먼저 들어간것이 가장 나중에 나오는 형태(선입후출,후입선출)

# 스택의 기본 구조
# 스택에 데이터를 삽입하는 작동 : push
# 스택에 데이터를 추출하는 작동 : pop
# 스택에 들어있는 가장 위의 데이터 : top

#스택의 생성

stack = [None, None, None, None, None] # 5개의 방이 있는 배열 생성
top = -1 # top 초기값 -1

#데이터 삽입 : push

top += 1
stack[top] = "커피"
top += 1
stack[top] = "녹차"
top += 1
stack[top] = "꿀물"

for i in range(len(stack)-1, -1 , -1):
    print(stack[i])

# 실행 결과 #
# None #
# None #
# 꿀물 #
# 녹차 #
# 커피 #

# 데이터 추출 : pop

stack = ["커피", "녹차", "꿀물", None, None]
top = 2

print("----- 스택 상태 -----")
for i in range(len(stack)-1, -1, -1):
    print(stack[i])
print("---------------------")

data = stack[top]
stack[top] = None
top -= 1
print("pop -->", data)

data = stack[top]
stack[top] = None
top -= 1
print("pop -->", data)

data = stack[top]
stack[top] = None
top -= 1
print("pop -->", data)

print("---------------------")

print("----- 스택 상태 -----")
for i in range(len(stack)-1, -1, -1):
    print(stack[i])

#실행 결과

# ----- 스택 상태 ----- #
# None #
# None #
# 꿀물 # 
# 녹차 #
# 커피 #
# --------------------- #
# pop --> 꿀물 #
# pop --> 녹차 #
# pop --> 커피 #
# --------------------- #
# ----- 스택 상태 ----- #
# None # 
# None #
# None #
# None #
# None #

# 스택 초기화

stack = [None, None, None, None, None] # 5개의 빈 방이 있는 스택 생성

SIZE = 5 # 스택 크기
stack = [None for _ in range(SIZE)]
top = -1

# 스택이 꽉 찼는지 확인하는 함수

def isStackFull():
    global SIZE,stack,top
    if(top>=SIZE-1):
        return True
    else:
        return False

SIZE = 5
stack = ["커피", "녹차", "꿀물", "콜라", "환타"]
top = 4

print("스택이 꽉 찼는지 여부 ---->", isStackFull())

# 출력 결과
# 스택이 꽉 찼는지 여부 ----> True

# 스택에 데이터를 삽입하는 함수

def push(data):
    global SIZE, stack, top
    if (top>=SIZE-1):
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

SIZE = 5
stack = ["커피", "녹차", "꿀물", "콜라", "환타"]
top = 3

print(stack)
push("환타")
print(stack)
push("게토레이")

# 실행 결과
# ['커피', '녹차', '꿀물', '콜라', '환타'] #
# ['커피', '녹차', '꿀물', '콜라', '환타'] #
# 스택이 꽉 찼습니다. #

# 스택이 비었는지 확인하는 함수

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False

SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

print("스택이 비었는지 여부 ==>", isStackEmpty())

# 실행 결과
# 스택이 비었는지 여부 ==> True #

# 스택에서 데이터를 추출하는 함수

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택이 비었습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

SIZE = 5
stack =["커피", None, None, None, None]
top = 0

print(stack)
retData = pop()
print("추출한 데이터 ==> ", retData)
print(stack)
retData = pop()

# 실행 결과

# ['커피', None, None, None, None] #
# 추출한 데이터 ==>  커피 #
# [None, None, None, None, None] #
# 스택이 비었습니다. #

# 스택에서 top의 위치의 데이터를 확인하는 함수

def isStackEmpty():
    global SIZE, stack, top
    if(top == -1):
        return True
    else:
        return False

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택이 비었습니다.")
        return None
    return [stack[top]]

SIZE = 5
stack = ["커피", "녹차", "꿀물", None, None]
top = 2

print(stack)
retData = peek()
print("top의 데이터 확인 ==> ", retData)
print(stack)

# 실행 결과
# ['커피', '녹차', '꿀물', None, None] #
# top의 데이터 확인 ==>  ['꿀물'] #
# ['커피', '녹차', '꿀물', None, None] #

# 스택 작동을 위한 통합 코드 #

def isStackFull(): # 스택이 꽉 찼는지 확인하는 함수
    global SIZE, stack, top
    if(top>=SIZE-1):
        return True
    else:
        return False

def isStackEmpty(): # 스택이 비었는지 확인하는 함수
    global SIZE, stack, top
    if(top == -1):
        return True
    else:
        return False

def push(data): # 스택에 데이터를 삽입하는 함수
    global SIZE, stack, top
    if (isStackFull()):
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

def pop(): # 스택에서 데이터를 추출하는 함수
    global SIZE,stack,top
    if (isStackEmpty()):
        print("스택이 비었습니다.")
        return None
    data = stack[top]
    stack[top]= None
    top -= 1
    return data

def peek(): # 스택에서 top 위치의 데이터를 확인하는 함수
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택이 비었습니다.")
        return None
    return stack[top]

# 전역 변수 선언 #

SIZE = int(input("스택 크기를 입력하세요 ==>"))
stack = [None for _ in range(SIZE)]
top = -1

# 메인 코드 #

if __name__ == "__main__":
    select = input("삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==> ")

    while (select !='X' and select !='x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 ==> ")
            push(data)
            print("스택 상태 : ", stack)

        elif select == 'E' or select == 'e':
            data = pop()
            print("추출된 데이터 ==>", data)
            print("스택 상태 : ", stack)
        
        elif select == 'V' or select == 'v':
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("스택 상태 : ", stack)

        else :
            print("입력이 잘못됨")

        select = input("삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==> ")

    print("프로그램 종료 !")

# 최종 실행 결과

# 스택 크기를 입력하세요 ==> 5 #
# 삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==> i #
# 입력할 데이터 ==> 치킨 #
# 스택 상태 :  ['치킨', None, None, None, None] #
# 삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==> i #
# 입력할 데이터 ==> 피자 #
# 스택 상태 :  ['치킨', '피자', None, None, None] #
# 삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==> i #
# 입력할 데이터 ==> 햄버거 #
# 스택 상태 :  ['치킨', '피자', '햄버거', None, None] #
# 삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==> i #
# 입력할 데이터 ==> 콜라 #
# 스택 상태 :  ['치킨', '피자', '햄버거', '콜라', None] #
# 삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==> i #
# 입력할 데이터 ==> 감자튀김 #
# 스택 상태 :  ['치킨', '피자', '햄버거', '콜라', '감자튀김'] #
# 삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==> e #
# 추출된 데이터 ==> 감자튀김 #
# 스택 상태 :  ['치킨', '피자', '햄버거', '콜라', None] #
# 삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==> v #
# 확인된 데이터 ==>  콜라 #
# 스택 상태 :  ['치킨', '피자', '햄버거', '콜라', None] #
# 삽입(I),추출(E),확인(V),종료(X) 중 하나를 선택 ==> x #
# 프로그램 종료 ! #
