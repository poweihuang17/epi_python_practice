def search_first_of_k(A,k):
	left, right, result= 0, len(A)-1, -1

	#A[left: right+1] is the target

	while left<=right:
		mid=left+(right-left)//2
		if A[mid] >k:
			right= mid-1

		elif A[mid]==k:
			right=mid-1
			result=mid

		else: 
			left=mid+1

	return result

A=[1,2,3,4,5,6,6,6,7,8,9,10]
k=6
print search_first_of_k(A,k)

