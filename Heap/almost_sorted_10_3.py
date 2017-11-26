import itertools
import heapq

def sort_almost_sorted(sequence,k):
	min_heap=[]
	result=[]
	for x in itertools.islice(sequence, k):
		heapq.heappush(min_heap,x)

	for x in itertools.islice(sequence,k,None):
		smallest=heapq.heappushpop(min_heap,x)
		result.append(smallest)

	while min_heap:
		remaining=heapq.heappop(min_heap)
		result.append(remaining)

	return result

if __name__ == '__main__':
	sequence=[3,-1,2,6,4,5,8]
	print sort_almost_sorted(sequence, 2)
