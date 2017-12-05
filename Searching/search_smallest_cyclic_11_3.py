def search_smallest(A):
	left, right= 0, len(A)-1

	while left<right:
		mid=left+(right-left)//2

		if A[mid]>A[right]:
			left=mid+1

		elif A[mid]<A[right]:
			right=mid

	return left

A=[378, 478, 550, 631, 103, 203, 220 ,234, 279, 368]
print search_smallest(A)

