def sum_root_to_leaf(tree, partial_path=0):

	if tree is None:
		return 0

	partial_path=partial_path *2+ tree.data

	# For leaf, return partial_path
	if not tree.left and not tree.right:
		return partial_path


	#For non-lef
	return sum_root_to_leaf(tree.left, partial_path)+sum_root_to_leaf(tree.right,partial_path)

class BinaryTreeNode:
	def __init__(self, data=None, left=None, right=None, parent=None):
		self.data=data
		self.left=left
		self.right=right
		self.parent=parent

if __name__ == '__main__':
	# Still need to implement a tree
	root, right, left=BinaryTreeNode(1),BinaryTreeNode(1), BinaryTreeNode(0)
	root.right=right
	root.left=left
	right.parent=root
	left.parent=root
	root.parent=root

	left_left=BinaryTreeNode(0)
	left_left_left=BinaryTreeNode(0)
	left_left_right=BinaryTreeNode(1)
	left.left=left_left
	left_left.parent, left_left_left.parent,left_left_right.parent=left,left_left,left_left
	left_left.left=left_left_left
	left_left.right=left_left_right

	print sum_root_to_leaf(root,0)