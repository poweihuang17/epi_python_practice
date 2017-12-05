import math 
def square_root(x):

	left, right= (x,1.0) if x< 1.0 else (1.0,x)

	while not math.isclose(left,right):
		mid=(left+right)*0.5

		if mid**2 > x:
			right=mid
		else:
		 	left=mid
	
	return left


print (square_root(3))


