class DoublylinkedlistNode:
	def __init__(self, data=None):
		self.data=data
		self.next=self.prev=None


class Doublylinkedlist:

	def __init__(self):
		self.head=self.tail=None
		self._size=0

	def __len__(self):
		return self._size

	def insert_after(self, value):
		node=DoublylinkedlistNode(value)
		node.prev=self.tail
		
		if self.tail:
			self.tail.next=node
		else:
			self.head=node

		self.tail=node
		self._size+=1

	def remove(self, node):
		# don't need to guard the dummy input node?

		if node.next:
			node.next.prev=node.prev
		else:
			self.tail=node.prev

		if node.prev:
			node.prev.next=node.next
		else:
			self.head=node.next

		node.next=node.prev=None
		self._size-=1


def find_smallest_subarray_covering_subset(stream, query_strings):
	last_occurence=Doublylinkedlist()
	# Initialize the dictionary
	d={s:None for s in query_strings} 
	result=(-1,-1)

	for index, s in enumerate(stream):
		if s in d:
			it=d[s]
			if it is not None:
				last_occurence.remove(it)

			last_occurence.insert_after(index)
			d[s]=last_occurence.tail

			if len(last_occurence)==len(query_strings):
				if result==(-1,-1) or index-last_occurence.head.data < result[1]-result[0]:
					result=(last_occurence.head.data, index)
	return result



paragraph=['apple', 'banana', 'apple', 'apple', 'dog', 'cat', 'apple', 'dog', 'banana', 'apple','cat', 'dog']
keywords=['banana', 'cat']

print find_smallest_subarray_covering_subset(paragraph, keywords)

