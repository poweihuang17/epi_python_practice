import heapq

def online_median(sequence):
	
	#Store the larger half
	min_heap=[]
	
	#Store the smaller half
	max_heap=[]

	for x in sequence:
		heapq.heappush(min_heap, x)
		if len(min_heap) > (len(max_heap)+1):
			heapq.heappush(max_heap, -heapq.heappop(min_heap))
	
	print len(min_heap)
	print len(max_heap)
	return (min_heap[0]-max_heap[0])/2.0 if len(min_heap)==len(max_heap) else min_heap[0]

if __name__ == '__main__':
	sequence=[0,0,1,2,3,5]
	print online_median(sequence)



