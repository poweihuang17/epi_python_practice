def find_nearest_repitition(paragraph):
	word_to_latest_index, min_distance={}, float('inf')

	for i, word in enumerate(paragraph):
		if word in word_to_latest_index:
			latest_index=word_to_latest_index[word]
			min_distance= min( i-latest_index, min_distance)
			#print "present"

		
		word_to_latest_index[word]=i
		#print i

	return min_distance

s=["All", "work","and", "no", "play", " makes", "for", "no", "work","no", "fun","and","no","results"]
#print len(s)
print find_nearest_repitition(s)