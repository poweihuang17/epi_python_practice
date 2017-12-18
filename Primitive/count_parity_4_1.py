# O(n) method
def count_parity_brute_forced(word):
	parity=0
	while word:
		parity ^= (word&1)
		word>>=1
	return parity


print count_parity_brute_forced(3)

#O(k) method

def count_parity_k(word):
	parity=0
	while word:
		parity^=1
		word=word & (word-1)

	return parity

print count_parity_k(3)
print count_parity_k(7)
