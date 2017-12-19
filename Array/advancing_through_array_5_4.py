def advancing_through_array(A):
	# input of A : list
	# output of A: bool

	farthest=0
	dp=[0]+[float('inf')]*(len(A)-1)

	for index, item in enumerate(A):

		if index > farthest:
			 success=False
			 break

		for j in range(1,item+1):
			if (index+j) >= len(A):
				break
			dp[index+j]=min(dp[index+j], dp[index]+1)

		#print dp

		farthest= max(farthest, index+item)

		if farthest==len(A)-1:
			success=True
			return (success, dp[len(A)-1])




	return (success, dp[len(A)-1])

print advancing_through_array([3,3,1,0,2,0,1])
print advancing_through_array([3,2,0,0,2,0,1])

