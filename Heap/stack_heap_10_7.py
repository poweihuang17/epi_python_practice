import heapq

class Stack:

	def __init__(self):
		self._timestamp=0 
		self._max_heap=[]

	def push(self.x):
		heapq.heappush(self._max_heap, (-self.timestamp, x))
		self._timestamp+=1

	def pop(self):
		if not self._max_heap:
			raise IndexError('Empty Stack')

		(mystamp, target) =heapq.heappop(self._max_heap)
		return target

	def peek(self):
		return self._max_heap[0][1]

