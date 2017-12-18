def even_odd(A):
	next_even, next_odd= 0, len(A)-1
	while next_even < next_odd:
		if A[next_even]%2==0:
			next_even+=1
		else:
			A[next_odd], A[next_even]=A[next_even], A[next_odd]
			next_odd-=1
	return A

if __name__ == "__main__":
	A=[1,3,2,4]
	print even_odd(A)