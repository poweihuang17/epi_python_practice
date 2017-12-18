def count_bits(x):
	num_bit=0
	while x:
		num_bit += (x&1)
		x>>=1
	return num_bit

if __name__=="__main__":
	print count_bits(15)
	print count_bits(31)
