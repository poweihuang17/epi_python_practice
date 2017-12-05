import random
import operator
def find_k_largest(k, A):

	def find_kth(comp):

		# Partition around pivot_idx
		# Return the new pivot after reorginzation

		def partition_around_pivot( left, right, pivot_idx):
			pivot_value= A[pivot_idx]
			new_pivot_idx= left
			A[pivot_idx], A[ right]= A[right], A[pivot_idx]

			for  i in range(left, right):
				if comp( A[i], pivot_value):
					A[i], A[new_pivot_idx]= A[new_pivot_idx], A[i]
					new_pivot_idx+=1

			A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]

			return new_pivot_idx

		left, right = 0, len(A)-1
		while left <= right:
			pivot_idx= random. randint(left, right)  # include both side.
			new_pivot_idx= partition_around_pivot(left, right, pivot_idx)
			if new_pivot_idx==(k-1):
				return A[new_pivot_idx]
			
			elif new_pivot_idx < (k-1):
				left= new_pivot_idx+1
			else:
				right=new_pivot_idx-1

	return find_kth(operator.gt)


A=[1,3,4,5,6,7,8,2]
print find_k_largest(3,A)

