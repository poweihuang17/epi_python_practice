# Find succesor
# Left 
def find_successor(node):
	#helper function. Leftmost
	def left_most(node):
		while node.left:
			node=node.left
		return node

	if node == None:
		return None
	#If node has a right subtree, find the leftmost node.
	elif node.right:
		return left_most(node.right)
	# node doesn't have a right subtree
	else:
		while node.parent and node.parent.right is node:
			node=node.parent
		return node.parent
