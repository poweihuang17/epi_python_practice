#This question is hard because it not only has to cover counting but also count the order.

import collections

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_sequentially_covering_subset(paragraph, keywords):
	keyword_to_idx= { k:i for i , k in enumerate(keywords) }

	latest_occurence=[-1]*len(keywords)

	shortest_subarray_length=[float('inf')]*len(keywords)