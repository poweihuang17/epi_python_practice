# Problem 9.4 -> find the lca when we have parent field on node.
def lca(node0, node1):
	def find_depth(node):
		depth=0
		while node.parent!=node:
			depth+=1
			node=node.parent
		return depth

	depth0=find_depth(node0)
	depth1=find_depth(node1)

	if depth1>depth0:
		diff=depth1-depth0
		for i in range(diff):
			node1=node1.parent
	else:
		diff=depth0-depth1
		for i in range(diff):
			node0=node0.parent

	while node0!=node1:
		node0=node0.parent
		node1=node1.parent

	return node0

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
