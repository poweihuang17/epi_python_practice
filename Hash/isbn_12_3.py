import collections

class LRUCache:
	def __init__(self,capacity):
		#Why we use order dictionary here?
		self._isbn_price_table = collections.OrderedDict()
		self._capacity= capacity

	def lookup(self, isbn):
		if isbn not in self._isbn_price_table:
			return False, None
		price= self._isbn_price_table[isbn]
		return True, price

	def insert(self, isbn, price):
		if isbn in self._isbn_price_table:
			#pop and insert again in order to update the order.
			price=self._isbn_price_table.pop(isbn)
		elif self._capacity <= len(self._isbn_price_table):
			#FIFO out
			self._isbn_price_table.popitem(last=False)

		self._isbn_price_table[isbn]=price

	def erase(self, isbn):
		return self._isbn_price_table.pop(isbn,None) is not None

cache= LRUCache(3)
cache.insert("12345", 12.0)
cache.insert("23456", 30.0)
print cache.lookup("12345")

print cache.erase("12345")

