#Why this solution is O(n)? Why the previous solution is O(n^2)?
#Because we find it repetitively. We should use double index to find!

RED, WHITE, BLUE= range(3)

def dutch_flag_partition(A, pivot_index):

	pivot=A[pivot_index]

	#Classify it into 4 classes.
	#So, use 3 indices.
	#Small, Middle  and Large.
	# 0: smaller -> smaller
	# smaller: equal -> equal
	# equal: large -> unclassified
	# [large:] -> larger
	smaller, equal, larger=0,0, len(A)

	while equal< larger:
		if A[equal] < pivot:
			A[smaller], A[equal]= A[equal], A[smaller]
			smaller, equal =smaller+1, equal+1

		elif A[equal] == pivot:
			equal+=1

		else:
			larger-=1
			A[larger], A[equal]= A[equal], A[larger]

A=[0,1,2,0,2,1,1]
dutch_flag_partition(A, 1)
print A