import collections

def is_balanced_binary_tree(tree):
	BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight',('balanced', 'height'))

	def check_balanced(tree):
		if not tree:
			return BalancedStatusWithHeight(True,-1)

		left_result=check_balanced(tree.left)
		if not left_result.balanced:
			return BalancedStatusWithHeight(False,0)

		right_result=check_balanced(tree.right)
		if not right_result.balanced:
			return BalancedStatusWithHeight(False,0)

		is_balanced=abs(left_result.height-right_result.height)<=1
		height=max(right_result.height, left_result.height)+1

		return BalancedStatusWithHeight(is_balanced,height)

	return check_balanced(tree).balanced

class BinaryTreeNode:
	def __init__(self, data=None, left=None, right=None):
		self.data=data
		self.left=left
		self.right=right

if __name__ == '__main__':
	# Still need to implement a tree
	root, right, left=BinaryTreeNode(),BinaryTreeNode(), BinaryTreeNode()
	root.right=right
	root.left=left

	left_left=BinaryTreeNode()
	left_left_left=BinaryTreeNode()
	left.left=left_left
	left_left.left=left_left_left

	print is_balanced_binary_tree(root)

