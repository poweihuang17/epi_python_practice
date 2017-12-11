import collections

class BSTNode:

	def __init__(self, data=None, left=None, right=None):
		self.data, self.left,self.right= data, left, right

#Solution 2 is BFS method
def is_binary_tree_bst(tree):

	entry= collections.namedtuple('entry', ( 'node', 'lower', 'upper'))

	bfs_queue=collections.deque([entry(tree, float('-inf'), float('inf'))])

	while bfs_queue:
		target=bfs_queue.popleft()
		if target.node:
			#print target.node.data
			if not target.lower<= target.node.data <= target.upper:
				#print target.lower
				#print target.upper
				#print target.node.data
				return False

			bfs_queue+= [entry(target.node.left, target.lower, target.node.data), entry(target.node.right, target.node.data, target.upper)]

	return True



if __name__ == '__main__':
	

	D=BSTNode(2)
	E=BSTNode(5)
	C=BSTNode(3, D, E)

	H=BSTNode(13)
	G=BSTNode(17,H)
	F=BSTNode(11,None, G)
	B=BSTNode(7, C,F)	
	
	M=BSTNode(31)
	L=BSTNode(29,None, M)

	N=BSTNode(41)

	K=BSTNode(37, L, N)

	J=BSTNode(23, None, K)

	P=BSTNode(53)
	O=BSTNode(47, None, P)
	I=BSTNode(43,J, O)

	A=BSTNode(19,B,I)

	print is_binary_tree_bst(A)