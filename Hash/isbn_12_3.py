class LRUCache:
	def __init__(self,capacity):
		self._isbn_price_table = collections.OrderedDict()
		self._capacity= capacity

	def lookup(self, isbn):
		if isbn not in self._isbn_price_table:
			return False, None
		price= self._isbn_price_table[isbn]
		return True, price