def swap_bit( word, i ,j):
	if word>>i  &1 != word>>j &1:
		bit_mask=(1<<i | 1 << j)
		word ^= bit_mask

	return word

print swap_bit(1, 0,2)