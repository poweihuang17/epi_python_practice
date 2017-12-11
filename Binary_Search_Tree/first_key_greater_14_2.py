def find_first_key(tree, number):
	while 


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

	print find_first_key(A,23)
