# python 큐 구현
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리를 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(5)
queue.append(5)
queue.append(5)
queue.popleft()
queue.append(5)
queue.append(5)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력