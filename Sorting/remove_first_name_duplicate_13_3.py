class Name:
	def __init__(self, first_name, last_name):
		self.first_name=first_name
		self.last_name=last_name

	def __eq__(self, other):
		#print self.first_name
		#print other.first_name
		return self.first_name ==other.first_name

	def __lt__(self, other):
		return self.first_name<other.first_name if self.first_name!= other.first_name else self.last_name < other.last_name

A=[Name('Ian', 'Botham'), Name('David', 'Gower'), Name('Ian', 'Bell'), Name('Ian', 'Chappell')]

def eliminate_duplicate(array):
	#print array
	array.sort()
	#print array
	#for name in array:
	#	print (name.first_name+' '+name.last_name)

	write_idx=1
	for cand in array[1:]:
		if not cand ==array[write_idx-1]:
			array[write_idx]=cand
			write_idx+=1
			#print 'different'
			#print write_idx

	del array[write_idx:]
	#print write_idx
	#print len(array)

eliminate_duplicate(A)

for name in A:
	print (name.first_name+' '+name.last_name)
	


