def matrix_search(A,x):
	row, column= 0, len(A[0])-1
	while row < len(A)  and  column>=0:
		if A[row][column] > x:
			column-=1
		elif A[row][column] <x:
			row+=1
		else:
			return True

	return False

A=[[-1,2,4,4,6], [1,5,5, 9, 21] , [3,6,7,9,22] , [3,6,8,10,24], [8,10,12,13,40]]

print matrix_search(A, 8)
print matrix_search(A,7)