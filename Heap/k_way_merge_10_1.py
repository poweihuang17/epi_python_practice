import heapq
def merge_sorted_arrays(sorted_arrays):
	min_heap=[]

	sorted_arrays_iters= [iter(x) for x in sorted_arrays]

	for i, it in enumerate(sorted_arrays_iters):
		first_element=next(it, None)
		if first_element is not None:
			heapq.heappush(min_heap, (first_element, i))

	result=[]
	while min_heap:
		smallest_entry, smallest_array_i= heapq.heappop(min_heap)

		result.append(smallest_entry)

		smallest_array_iter=sorted_arrays_iters[smallest_array_i]
		next_element=next(smallest_array_iter,None)
		if next_element is not None:
			heapq.heappush(min_heap, (next_element, smallest_array_i))
	return result

if __name__ == '__main__':
	a=[ [1,2,3], [3,4,5,6], [0,1,9,10,11] ]
	print merge_sorted_arrays(a)


