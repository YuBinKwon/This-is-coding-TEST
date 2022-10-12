# 스택

stack=[]

stack.append(5) #가장 뒤쪽에 데이터 삽입
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() #가장 뒤쪽의 데이터 삭제
stack.append(1)
stack.append(4)
stack.pop()

print(stack) #최하단 원소부터 출력
print(stack[::-1]) #최상단 원소부터 출력
# [5,2,3,1]
# [1,3,2,5]

#-------------------------------------------
# 큐 : 선입선출 구조 (first in first out)

from collections import deque
#큐 구현을 위해 deque 라이브러리  사용
queue=deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력
queue.reverse() #역순으로 바꾸기
print(queue) #나중에 들어온 원소부터 출력
# deque([3,7,1,4])
# deque([4,1,7,3])

# list(queue) 하면 리스트 자료형으로 반환

#-------------------------------------------
# 재귀 함수

#팩토리얼 함수
#반복적으로 구현
def factorial_iterative(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

#재귀적으로 구현
def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)


