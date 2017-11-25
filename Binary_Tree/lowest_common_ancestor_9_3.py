## 1118: This is really difficult....
import collections
def find_lca(tree, node0, node1):
	Status = collections.namedtuple('Status',('number_of_node', 'tree'))

	def lca_helper(tree, node0, node1):

		if not tree:
			return Status(0, None)

		left_result=lca_helper(tree.left,node0, node1)
		if left_result.number_of_node==2:
			return left_result

		right_result=lca_helper(tree.right, node0, node1)
		if right_result.number_of_node==2:
			return right_result

		node_now=left_result.number_of_node+right_result.number_of_node+int(tree==node0)+int(tree==node1)

		return Status(node_now, tree if node_now==2 else None)

	return lca_helper(tree,node0,node1).tree

class BinaryTreeNode:
	def __init__(self, data=None, left=None, right=None):
		self.data=data
		self.left=left
		self.right=right


if __name__ == '__main__':
	# Still need to implement a tree
	root, right, left=BinaryTreeNode(0),BinaryTreeNode(1), BinaryTreeNode(2)
	root.right=right
	root.left=left

	left_left=BinaryTreeNode(3)
	left_left_left=BinaryTreeNode(4)
	left.left=left_left
	left_left.left=left_left_left
	left_left_right=BinaryTreeNode(5)
	left_left.right=left_left_right

	print find_lca(root,left_left_left, left_left_right ).data