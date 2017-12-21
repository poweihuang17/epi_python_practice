import itertools
import pdb

class ListNode:

	def __init__(self, data=0, next_node=None):
		self.data=data
		self.next=next_node

class List:

	def __init__(self,node_list):

		self.head=node_list[0]

		node_now=self.head

		for node in itertools.islice(node_list,1,None):
			node_now.next=node
			node_now=node

	def custom_print(self):

		target=self.head
		while target:
			print target.data
			target=target.next


	def search_list(self,key):
		#If key is not in the list, 
		while self and self.data!=key:
			L=L.next
		return L

	def insert_node(self,node, new_node):
		new_node.next=node.next
		node.next=new_node


	def delete_node(self,node):
		#Delete the node past this node. Assume it's not a tail.
		node.next=node.next.next
		# Question: how to do delete in python.


mylist1=List([ListNode(2), ListNode(5), ListNode(7)])


def print_linked_list_in_reserve(head):
	nodes=[]
	while head:
		nodes.append(head.data)
		head=head.next
	while nodes:
		print nodes.pop()

print_linked_list_in_reserve(mylist1.head)

