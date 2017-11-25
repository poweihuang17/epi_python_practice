def bst_in_sorted_order(tree):
	
	s, result=[], []

	while s or tree:
		if tree:
			s.append(tree)
			#Going left
			tree=tree.left
			#raw_input()
		else:
			#Going up
			tree=s.pop()
			result.append(tree.data)
			#Going right
			tree=tree.right
			#raw_input()

	return result
