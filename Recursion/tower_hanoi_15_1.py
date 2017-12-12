def compute_tower_hanoi(num_rings):
	if num_rings is 1:
		return 1
	else:
		return 2*compute_tower_hanoi(num_rings-1)+1

print compute_tower_hanoi(3)


count=100

def hanoi_problem(num_rings,from_peg, to_peg, use_peg):
	count=0

	def compute_the_step(num_rings,from_peg, to_peg, use_peg):
		global count
		if num_rings==1:
			print 'Move from peg '+str(from_peg)+' to '+str(to_peg)
			print count
			count+=1
			return None

		compute_the_step(num_rings-1, from_peg, use_peg, to_peg)
		print count
		count+=1
		print 'Move from peg '+str(from_peg)+' to '+str(to_peg)
		compute_the_step(num_rings-1, use_peg, to_peg, from_peg)
	
	compute_the_step(num_rings,from_peg, to_peg, use_peg)

	return count


print count

print hanoi_problem(3,0,1,2)
print count

	