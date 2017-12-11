def gcd(x,y):
	return x if y==0 else gcd(y, x%y)


print gcd(35,5)