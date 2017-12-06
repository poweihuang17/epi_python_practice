def smallest_constructible(A):
	max_constructible_value=0
	for a in sorted(A):
		if a > max_constructible_value+1:
			break
		max_constructible_value+=a
	return max_constructible_value+1

A=[12,2,1,15,2,4]
print smallest_constructible(A)