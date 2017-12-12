def compute_tower_hanoi(num_rings):
	count=0
	def hanoi_problem(num_rings_to_move,from_peg, to_peg, use_peg):
		nonlocal count
		if num_rings_to_move>0:
			hanoi_problem(num_rings_to_move-1,from_peg, use_peg, to_peg)
			pegs[to_peg].append(pegs[from_peg].pop())
			count+=1
			print('Move from peg '+str(from_peg)+' to '+str(to_peg))
			hanoi_problem(num_rings_to_move-1, use_peg, to_peg, from_peg)
		return count

	NUM_PEGS=3
	pegs=[list( reversed( range(1,num_rings+1) ))] + [[] for _ in range(1, NUM_PEGS)]
	print(hanoi_problem(num_rings,0,1,2))

compute_tower_hanoi(3)
 

