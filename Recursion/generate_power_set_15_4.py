import math

def generate_power_set_1(input_set):

	def directed_power_set(to_be_selected, selected_so_far):
		if to_be_selected is len(input_set):
			power_set.append(list(selected_so_far))
			return 

		directed_power_set(to_be_selected+1, selected_so_far)

		directed_power_set(to_be_selected+1, selected_so_far+ [input_set[to_be_selected]])



	power_set=[]
	directed_power_set(0, [])

	return power_set


power_set = generate_power_set_1([1,2,3,4])
print(len(power_set))
print(power_set)

def generate_power_set_2(S):
	power_set=[]
	for int_for_subset in range(1<<len(S)):
		bit_array=int_for_subset
		subset=[]
		while bit_array:
			subset.append(S[int(math.log2(bit_array & ~(bit_array-1)))])
			bit_array &= bit_array-1
		power_set.append(subset)

	return power_set

power_set_2=generate_power_set_2([1,2,3,4])
print(len(power_set_2))
print(power_set_2)

