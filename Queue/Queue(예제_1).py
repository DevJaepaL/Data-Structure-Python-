# 유명 맛집의 대기줄에는 손님들이 들어온 순서대로 줄을 선다.
# 그리고 대기줄이 꽉 차면 더이상 손님을 받지 않는다.
# 이제 대기줄 손님들은 자리가 생기면 1명씩 식당으로 들어간다.
# 맨 앞쪽 손님이 대기줄에서 식당으로 들어갈 때 마다 대기줄 뒤쪽 손님들은
# 한칸 씩 이동해서 줄을 다시 서도록 한다.

# ==== 문제 풀이 ====

# - 함수 부분 -
def EnQueue(data):
    global SIZE,queue,front,rear
    rear += 1
    queue[rear] = data

def DeQueue():
    global SIZE,queue,front,rear
    front += 1
    data = queue[front]
    queue[front] = None

    for i in range(front + 1, rear + 1):
        queue[i - 1] = queue[i]
        queue[i] = None
    front = -1
    rear -= 1

    return data

# - 전역 변수 -
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

# - 메인 코드 -
if __name__ == "__main__":
    EnQueue("정국")
    EnQueue("뷔")
    EnQueue("지민")
    EnQueue("진")
    EnQueue("슈가")
    print("대기 줄 상태 : ", queue)

    for _ in range(rear+1):
        print(DeQueue(), "님 식당에 들어감")
        print("대기 줄 상태 : ", queue)

    print("식당 영업 종료 !")
    

# ==== 문제 정답 ==== #

대기 줄 상태 :  ['정국', '뷔', '지민', '진', '슈가']
정국 님 식당에 들어감
대기 줄 상태 :  ['뷔', '지민', '진', '슈가', None]
뷔 님 식당에 들어감
대기 줄 상태 :  ['지민', '진', '슈가', None, None]
지민 님 식당에 들어감
대기 줄 상태 :  ['진', '슈가', None, None, None]
진 님 식당에 들어감
대기 줄 상태 :  ['슈가', None, None, None, None]
슈가 님 식당에 들어감
대기 줄 상태 :  [None, None, None, None, None]
식당 영업 종료 !