def generate_all_subset(n,k):

	def directed_combinations(offset, partial_combination):
		if len(partial_combination) is k:
			result.append(list(partial_combination))
			return

		num_remaining = k-len(partial_combination)
		i=offset

		while i<=n and num_remaining<= n-i+1:
			directed_combinations(i+1, partial_combination+[i])
			i+=1



	result, partial_combination=[], []
	directed_combinations(1, partial_combination)
	return result

A=generate_all_subset(5,3)
print A
print len(A)