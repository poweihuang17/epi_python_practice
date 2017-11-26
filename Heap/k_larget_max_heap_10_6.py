import heapq

def k_larget(A,k):
	if k<0:
		return None

	max_heap=[]
	max_heap.append((-A[0],0))

	result=[]

	for _ in range(k):
		
		index=max_heap[0][1]
		result.append(-heapq.heappop(max_heap)[0])

		left_index=index*2+1
		if left_index<len(A):
			heapq.heappush(max_heap,(-A[left_index],left_index))

		right_index=index*2+2
		if right_index<len(A):
			heapq.heappush(max_heap,(-A[right_index],right_index))


	return result


if __name__ == '__main__':
	sequence=[561,314,401,28,156,359,271,11,3]
	print k_larget(sequence,4)



