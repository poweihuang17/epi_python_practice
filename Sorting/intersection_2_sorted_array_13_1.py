import bisect

def intersect_two_sorted_arrays_brute_forced(A,B):
	return [a for i, a  in enumerate(A) if (i==0 or a!=A[i-1]) and a in B]

A=[2,3,3,5,5,6,7,7,8,12]
B=[5,5,6,8,8,9,10,10]

print intersect_two_sorted_arrays_brute_forced(A,B)

def intersect_two_sorted_arrays_bisect(A,B):

	def is_present(k):
		i=bisect.bisect_left(B,k)
		return i<len(B) and B[i]==k


	return [a for i, a  in enumerate(A) if (i==0 or A[i-1]!=a) and is_present(a) ]

print intersect_two_sorted_arrays_bisect(A,B)	

def intersect_two_by_advance(A,B):
	i, j=0,0
	result=[]
	while i <len(A) and j<len(B):
		if A[i]==B[j]:
			if i==0 or A[i] != A[i-1]:
				result.append(A[i])
			i,j= i+1, j+1

		elif A[i]<B[j]:
			i+=1

		else:
			j+=1

	return result

print intersect_two_by_advance(A,B)
