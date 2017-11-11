class ListNode:

	def __init__(self, data=0, next_node=None):
		self.data=data
		self.next=next_node

	def search_list(L,key):
		#If key is not in the list, 
		while L and L.data!=key:
			L=L.next
		return L

	def insert_node(node, new_node):
		new_node.next=node.next
		node.next=new_node


	def delete_node(node):
		#Delete the node past this node. Assume it's not a tail.
		node.next=node.next.next
		# Question: how to do delete in python.