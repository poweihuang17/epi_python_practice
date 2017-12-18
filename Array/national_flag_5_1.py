#Why this solution is O(n^2)?

RED, WHITE, BLUE= range(3)

def dutch_flag_partition(A, pivot_index):
		pivot=A[pivot_index]
		#First pass : group elements samller than pivot
		for i in range(len(A)):
			for j in range(i+1, len(A)):
				if A[j]<pivot:
					A[j], A[i]= A[i], A[j]
					break

		#Second pass : group elements larger than pivot
		for i in reversed(range(len(A))):
			#Still don't know why do we need this.
			if A[i] < pivot:
				break

			for j in reversed(range(i)):
				if A[j] > pivot:
					A[j], A[i] = A[i], A[j]
					break

A=[0,1,2,0,2,1,1]
dutch_flag_partition(A, 3)
print A



