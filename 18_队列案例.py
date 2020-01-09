from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print('popleft：', queue.popleft())
print('popleft：', queue.popleft())
print('queue：', queue)



