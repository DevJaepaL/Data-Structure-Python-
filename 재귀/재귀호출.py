# 재귀란 ?
#   양쪽에 거울이 있을 때, 거울에 비친 자신이 무한 반복해서 비치는 것.
#   마트료시카 인형처럼 동일한 작동을 무한적으로 반복하는 알고리즘이다.

# 재귀 호출의 개념.
#   재귀 호출(Recursion)은 자신을 다시 호츌하는 것.

# 재귀 호출 함수의 기본
def openBox():
    global count,cnt
    print("종이 상자를 엽니다.", count)
    count -= 1
    if count == 0:
        print("* 반지를 넣고 반환합니다. *")
        return
    openBox()
    cnt += 1
    print("종이 상자를 닫습니다.", cnt)

count = 10
cnt = 0
openBox()

# 실행결과 
    종이 상자를 엽니다. 10
    종이 상자를 엽니다. 9
    종이 상자를 엽니다. 8
    종이 상자를 엽니다. 7
    종이 상자를 엽니다. 6
    종이 상자를 엽니다. 5
    종이 상자를 엽니다. 4
    종이 상자를 엽니다. 3
    종이 상자를 엽니다. 2
    종이 상자를 엽니다. 1
    * 반지를 넣고 반환합니다. *
    종이 상자를 닫습니다. 2
    종이 상자를 닫습니다. 3
    종이 상자를 닫습니다. 4
    종이 상자를 닫습니다. 5
    종이 상자를 닫습니다. 6
    종이 상자를 닫습니다. 7
    종이 상자를 닫습니다. 8
    종이 상자를 닫습니다. 9

# 재귀 함수로 10부터 1까지의 합계를 구현
def addNum(num):
    if num<=1:
        return 1
    return num + addNum(num-1)

print(addNum(10))

# 실행 결과 
    55

# 재귀 함수로 팩토리얼 구현
def factorial(num):
    if num <= 1:
        print("1 의 값 반환")
        return 1
    print("%d * %d! 호출" % (num,num-1))
    retVal = factorial(num-1)

    print ("%d * %d! (=%d) 반환" % (num, num-1, retVal))
    return num * retVal

print("5! = ",factorial(5))

# 실행결과
    5 * 4! 호출
    4 * 3! 호출
    3 * 2! 호출
    2 * 1! 호출
    1 의 값 반환
    2 * 1! (=1) 반환
    3 * 2! (=2) 반환
    4 * 3! (=6) 반환
    5 * 4! (=24) 반환
    5! =  120

# 재귀 호출로 간단한 별 모양 출력
def printStar(n):
    if n > 0:
        printStar(n-1)
        print('★' * n)

printStar(5)

# 실행 결과
    ★
    ★★
    ★★★
    ★★★★
    ★★★★★

# 재귀 호출로 배열의 합계 구현
import random

def arySum(arr,n):
    if n <= 0 :
        return arr[0]
    return arySum(arr, n-1) + arr[n]

ary = [random.randint(0,255) for _ in range
        (random.randint(1,10))]

print(ary)
print("배열의 합계 ==>", arySum(ary,len(ary)-1))

# 실행결과
    [65, 254, 99, 159, 17, 150, 15, 52]
    배열의 합계 ==> 811

# 회문 여부 구별

def palindrome(pStr):
    if len(pStr) <= 1:
        return True

    if pStr[0] != pStr[-1]:
        return False

    return palindrome(pStr[1:len(pStr)-1])

strAry = ["reaver", "kayak", "Borrow or rob", "주유소의 소유주"]

for testStr in strAry:
    print(testStr, end = ' ==> ')
    testStr = testStr.lower().replace(' ','')
    if palindrome(testStr):
        print('O')
    else:
        print('X')

# 실행결과
    reaver ==> X
    kayak ==> O
    Borrow or rob ==> O
    주유소의 소유주 ==> O

# 간단한 원을 그리는 GUI
from tkinter import *

window = Tk()
wSize = 1000
canvas = Canvas(window, height=wSize,width=wSize, bg='white')
canvas.pack()

cx = 1000//2
cy = 1000//2
r = 400
canvas.create_oval(cx-r,cy-r,cx+r,cy+r,width=2,outline="red")

window.mainloop()

# GUI를 이용해 재귀호출을 사용하여 간단한 프랙탈 만들기
from tkinter import*

def drawCircle(x,y,r):
    global count
    count += 1
    print('x =',x,'y =',y,'r =',r)
    canvas.create_oval(x-r,y-r,x+r,y+r)
    canvas.create_text(x,y-r,text=str(count),font=('',30))
    if r >= radius/2:
        drawCircle(x-r//2, y, r//2) # 재귀 호출 부분
        drawCircle(x+r//2, y, r//2) # 재귀 호출 부분

count = 0
wSize = 500
radius = 200

window = Tk()
canvas = Canvas(window,height=wSize,width=wSize,bg='white')

drawCircle(wSize//2,wSize//2,radius)

canvas.pack()
window.mainloop()