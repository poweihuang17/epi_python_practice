import bintrees

class BSTNode:

	def __init__(self, data=None, left=None, right=None):
		self.data, self.left,self.right= data, left, right


t = bintrees.RBTree([ (5,'Alfa'), (2, 'Bravo'), (7,'Charlie'), (3,'Delta'), (6, 'Echo')])
print t[2]

print (t.min_item(), t.max_item())

t.insert(9, 'Golf')

print (t)

print (t.min_key(), t.max_key())


