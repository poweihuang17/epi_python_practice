def search_entry_equal_index(A):
	left, right= 0 , len(A)-1
	#A[left: right+1] is the range
	while left <= right:
		mid= left+(right-left)//2

		if A[mid] < mid:
			left=mid+1

		elif A[mid]==mid:
			return mid

		else:
			#A[mid] > mid
			right=mid-1
	return -1

A=[-2, 0 , 2, 3,6,7,9]
print search_entry_equal_index(A)