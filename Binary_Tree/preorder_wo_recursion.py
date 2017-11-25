def bst_pre_sorted_order(tree):
	path, result=[tree],[]

	if tree is None:
		return []
	
	while path:
		tree=path.pop()
		
		if tree.right is not None:
			path.append(tree.right)
		if tree.left is not None:
			path.append(tree.left)

		result.append(tree)

	return result


