from collections import deque
import fileinput

queue = deque()

for line in fileinput.input():
    inputs = line.rstrip().split()
    if inputs[0] == '1':
        queue.append(inputs[1])
    if inputs[0] == '2':
        queue.popleft()
    if inputs[0] == '3':
        print(queue[0])
