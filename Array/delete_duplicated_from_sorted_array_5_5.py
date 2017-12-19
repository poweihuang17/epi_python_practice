def delete_duplicated(A):
	target=0
	temp=float('inf')
	for index, item in enumerate(A):
		#Not duplicate
		if item!=temp:
			A[target]=item
			temp=item
			target+=1
		
		#Duplicate
		#Do nothing

	return (A, target)


print delete_duplicated([2,3,5,5,7,11,11,11,13])

			