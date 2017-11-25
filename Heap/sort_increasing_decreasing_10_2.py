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

def sort_k_increasing_decreasing(A):
	#First, I have to cut the array into k increasing and decreasing arrays.
	INCREASING, DECREASING= range(2)
	sorted_subarrays=[]
	subarray_type=INCREASING
	start_idx=0

	for i in range(1,len(A)+1):
		#To cover the last element
		if i==len(A) and subarray_type is INCREASING:
			sorted_subarrays.append(a[start_idx:i])

		elif i==len(A) and subarray_type is DECREASING:
			sorted_subarrays.append(a[i-1:start_idx-1:-1])

		elif a[i-1]> a[i] and subarray_type is INCREASING:
			sorted_subarrays.append(a[start_idx:i])
			start_idx=i
			subarray_type=DECREASING

		elif a[i-1]<a[i] and subarray_type is DECREASING:
			sorted_subarrays.append(a[i-1:start_idx-1:-1])
			start_idx=i
			subarray_type=INCREASING
	return merge_sorted_arrays(sorted_subarrays)
 
if __name__ == '__main__':
	a=[ 1,3,5,7,5,3,1,3,5,7, 6, 5 ,4 ,3 ,2 ,3 ,4 ,5 ]
	print sort_k_increasing_decreasing(a)
