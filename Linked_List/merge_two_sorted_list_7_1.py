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
mylist2=List([ListNode(3), ListNode(11)])

mylist1.custom_print()
mylist2.custom_print()

print " "

def merge_two_sorted_lists_my_solution(L1,L2):
	index1=L1.head
	index2=L2.head
	
	if index1.data >= index2.data:
		new_head=L2
		index2 ,index2.next =index2.next, index1
	else:
		new_head=L1
		L2.head=index1
		index1, index1.next= index1.next, index2
		

	pdb.set_trace()
	while index1 and index2:
		if index1.data >= index2.data:
			index2 ,index2.next =index2.next, index1
		else:
			index1, index1.next= index1.next, index2
		print "merging:"+str(index1.data) +" "+str(index2.data)
		L1.custom_print()
		print " "
		L2.custom_print()

	return new_head

#merge_two_sorted_lists(mylist1, mylist2).custom_print()

def merge_two_sorted_lists( L1, L2):
	dummy_head=tail=ListNode()

	while L1 and L2:
		if L1.data<L2.data:
			tail.next, L1 = L1, L1.next
		else:
			tail.next, L2 =L2, L2.next
		tail=tail.next
	
	tail.next=L1 or L2
	return dummy_head.next

result=merge_two_sorted_lists(mylist1.head, mylist2.head)

while result:
	print result.data
	result=result.next

