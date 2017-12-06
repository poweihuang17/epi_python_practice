def merge_two_sorted_arrays(A, m , B, n):
	a,b, write_idx= m-1, n-1, m+n-1
	while a>=0 and b>=0:
		if A[a]>B[b]:
			A[write_idx]=A[a]
			a-=1

		elif A[a]<B[b]:
			A[write_idx]=B[b]
			b-=1

		else:
			A[write_idx]=A[a]
			A[write_idx-1]=A[a]
			a-=1
			b-=1

		write_idx-=1

	while b>=0:
		A[write_idx]=B[b]
		write_idx, b= write_idx-1, b-1

A=[5,13,17,0,0,0,0]
B=[3,7,11,19]
merge_two_sorted_arrays(A,3,B,4)
print A

#List is not copy for function call...
#When could we copy?


		