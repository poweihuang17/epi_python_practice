def has_path_sum(tree, remaining_weight):
	if not tree:
		return False

	remaining_weight-=tree.data

	#Leaf
	if not tree.right and not tree.left:
		return True if remaining_weight is 0 else False

	#Non leaf
	return has_path_sum(tree.right, remaining_weight) or has_path_sum(tree.left, remaining_weight)