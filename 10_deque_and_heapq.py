from collections import deque  
# deque = "pronounced 'deck' "

queue = deque()
# or
q = deque([4, 5, 6, 7, 8])

queue.append(10)
queue.append(15)
queue.append(20)

queue.appendleft(5)

queue.pop()
queue.popleft()




import heapq # used to find the min and max of a set of values frequently
# in python heapq, is a min heap



# under the hood are array
minHeap = []
heapq.heappush(minHeap, 3) # to push value 3
heapq.heappush(minHeap, 5)
heapq.heappush(minHeap, 7)

# Min is always at index 0
print("Min is: ", minHeap[0])

while len(minHeap):
	print(heapq.heappop(minHeap))



# No max heap, but multiply by -1 when push & pop
maxHeap = []
heapq.heappush(maxHeap, -5)
heapq.heappush(maxHeap, -8)
heapq.heappush(maxHeap, -9)

# Max at index 0
print("Max is: ", -1 * maxHeap[0])

while len(maxHeap):
	print(-1 * heapq.heappop(maxHeap))



# Build a heap from initial values
array = [2, 6, 7, 3, 4]
heapq.heapify(array)
while array:
	print(heapq.heappop(array))
	