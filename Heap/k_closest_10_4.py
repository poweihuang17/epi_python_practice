import heapq
class Star:
	def __init__(self,x,y,z):
		self.x,self.y,self.z=x,y,z

	# Still don't know property....
	@property
	def distance(self):
		return math.sqrt(self.x**2+self.y**2+self.z**2)

	def __lt__(self,rhs):
		return self.distance <rhs.distance

def find_closest_k_stars(stars, k):
	max_heap=[]

	for star in stars:
		heapq.heappush(max_heap, (-star.distance,star))
		if len(max_heap)==(k+1) :
			heapq.heappop(max_heap)

	return s[1] for s in heapq.nlargest(k,max_heap)
	#nlargest 回傳k個最大的。那順序是如何呢？