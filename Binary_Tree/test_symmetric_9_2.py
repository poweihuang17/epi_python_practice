def is_symmetric(tree):
	def check_subtree(subtree1,subtree2):
		#Both trees are empty
		if not subtree1 and not subtree2:
			return True
		#Both trees exist
		elif subtree1 and subtree2:
			return subtree1.data==subtree2.data and check_subtree(subtree1.right,subtree2.left) and check_subtree(subtree1.left, subtree2.right)
		#Only one tree exists
		else:
			return False

	return not tree or check_subtree(tree.right,tree.left)

class BinaryTreeNode:
	def __init__(self, data=None, left=None, right=None):
		self.data=data
		self.left=left
		self.right=right


if __name__ == '__main__':
	# Still need to implement a tree
	root, right, left=BinaryTreeNode(0),BinaryTreeNode(0), BinaryTreeNode(0)
	root.right=right
	root.left=left

	#left_left=BinaryTreeNode()
	#left_left_left=BinaryTreeNode()
	#left.left=left_left
	#left_left.left=left_left_left

	print is_symmetric(root)