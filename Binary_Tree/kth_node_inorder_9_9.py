def find_kth_inorder(tree, k):

	if k is 1:
		return tree

	if (k-1) <= tree.left.number:
		find_kth_inorder(tree.left,k-1)
	elif k>(tree.left.number+1):
		find_kth_inorder(tree.right,k-(tree.left.number+1))
	return None