import functools

def string_hash(s,modulus):
	MULT=997
	return functools.reduce(lambda v,c : (v*MULT+ord(c)) % modulus, s, 0 )

if __name__ == '__main__':
	s="abc"
	modulus=100
	print string_hash(s,100)