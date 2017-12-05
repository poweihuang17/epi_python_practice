def square_root(k):
	left, right=0,k-1

	#[left, right+1] is the range that's equal to or smaller to.
	while left<=right:

		mid= left+(right-left)//2
		
		#print mid
		#print " "+str(left)+" "+str(right)

		if mid**2 <k :
			left=mid+1
		elif mid**2 ==k:
			return mid
		else:
			right=mid-1
	
	return left-1



k=21
print square_root(k)
k=300
print square_root(k)