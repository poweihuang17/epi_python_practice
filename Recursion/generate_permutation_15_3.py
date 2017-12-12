def permutations_1(A):

	def directed_permutation(n):

		if n is len(A)-1:
			result.append(list(A))
			return

		for i in range(n, len(A)):
			A[n],A[i]=A[i],A[n]

			directed_permutation(n+1)

			A[n],A[i]=A[i],A[n]




	result=[]
	directed_permutation(0)
	return result

myresult=permutations_1([1,2,3,4,5])

print myresult
print len(myresult)

#def permutation_2(A):


