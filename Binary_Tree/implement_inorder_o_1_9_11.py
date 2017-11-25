# Need to use 

def inorder_traversal(tree):
	prev, result= None,[]
	while tree.left:
		tree=tree.left

