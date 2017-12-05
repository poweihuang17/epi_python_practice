def lca(node_0, node_1):
	iter_0, iter_1= node_0, node_1
	nodes_on_path_to_root=set()

	while iter_0 or iter_1:
		if iter_0:
			if iter_0 in nodes_on_path_to_root:
				return iter_0
			nodes_on_path_to_root.add(iter_0)
			iter_0=iter_0.parent

		if iter_1:
			if iter_1 in nodes_on_path_to_root:
				return iter_1
			nodes_on_path_to_root.add(iter_1)
			iter_1=iter_1.parent

	raise ValueError('node_0 and node_1 are not in the same tree')

class BinaryTreeNode:
	def __init__(self, data=None, left=None, right=None, parent=None):
		self.data=data
		self.left=left
		self.right=right
		self.parent=parent

if __name__ == '__main__':
	# Still need to implement a tree
	root, right, left=BinaryTreeNode(0),BinaryTreeNode(1), BinaryTreeNode(2)
	root.right=right
	root.left=left
	right.parent=root
	left.parent=root
	root.parent=root

	left_left=BinaryTreeNode(3)
	left_left_left=BinaryTreeNode(4)
	left_left_right=BinaryTreeNode(5)
	left.left=left_left
	left_left.parent, left_left_left.parent,left_left_right.parent=left,left_left,left_left
	left_left.left=left_left_left
	left_left.right=left_left_right

	print lca(left_left_left, left_left_right ).data