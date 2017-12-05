import collections
MinMax= collections.namedtuple('MinMax', ('smallest', 'biggest'))

def find_min_max(A):

	def min_max(a,b):
		return MinMax(a,b) if a < b else MinMax(b,a)

	if len(A)<=1:
		return MinMax(A[0], A[0])

	global_min_max= min_max(A[0], A[1])

	for  i in range(2, len(A)-1,2):
		local_min_max=min_max(A[i], A[i+1])

		global_min_max=MinMax(min(local_min_max.smallest, global_min_max.smallest) 
			, max(local_min_max.biggest, global_min_max.biggest))

	if len(A)%2:
		global_min_max=MinMax(min(A[-1], global_min_max.smallest) 
			, max(A[-1], global_min_max.biggest))

	return global_min_max

A=[2,5,1,2,4,3,6,7, 0, -3]
print find_min_max(A)
