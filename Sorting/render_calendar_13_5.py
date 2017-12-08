import collections

Event=collections.namedtuple('Event', ('start', 'end'))

Endpoint=collections.namedtuple('Endpoint', ('time', 'is_start'))

def find_max_simultaneous_event(A):
	#All the endpoints
	E=[Endpoint(event.start, True) for event in A]+[Endpoint(event.end, False) for event in A]
	
	#Find 
	E.sort(key=lambda e: (e.time, not e.is_start))

	count=0
	max_count=0

	for e in E:
		if e.is_start:
			count+=1
		else:
			count-=1

		if count>max_count:
			max_count=count

	return max_count





if __name__ == '__main__':

	A={ Event(Endpoint(1.0, True) , Endpoint(5.0, False)), Event(Endpoint(2.0, True), Endpoint(7.0, False)),Event(Endpoint(4.0,True),Endpoint(5.0,False)), Event(Endpoint(6.0, True),Endpoint(10.0,False)),Event(Endpoint(8.0, True),Endpoint(9.0,False)), Event(Endpoint(9.0,True),Endpoint(17.0,False)), Event(Endpoint(11.0,True),Endpoint(13.0,False)), Event(Endpoint(12.0,True),Endpoint(15.0,False)), Event(Endpoint(14.0,True),Endpoint(15.0,False))}
	print find_max_simultaneous_event(A)