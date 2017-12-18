#Why this solution is O(n)? Why the previous solution is O(n^2)?
#Because we find it repetitively. We should use double index to find!

RED, WHITE, BLUE= range(3)

def dutch_flag_partition(A, pivot_index):

		pivot=A[pivot_index]
		#Single pass : group elements samller than pivot
		smaller=0
		for i in range(len(A)):
			if A[i] < pivot:
				A[i],A[smaller]=A[smaller], A[i]
				smaller+=1


		#Second part of the single pass:
		# group elements bigger than 
		larger= len(A)-1

		for i in reversed(range(len(A))):
			# Meet the group of smaller parts. 
			if A[i] < pivot:
				break

			if A[i] > pivot:
				A[larger], A[i] = A[i], A[larger]
				larger-=1

A=[0,1,2,0,2,1,1]
dutch_flag_partition(A, 1)
print A