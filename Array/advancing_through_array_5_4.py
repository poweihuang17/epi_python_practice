def advancing_through_array(A):
	# input of A : list
	# output of A: bool

	farthest=0
	for index, item in enumerate(A):
		if index > farthest:
			return False

		farthest= max(farthest, index+item)

		if farthest==len(A)-1:
			return True

print advancing_through_array([3,3,1,0,2,0,1])
print advancing_through_array([3,2,0,0,2,0,1])

