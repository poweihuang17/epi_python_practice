import collections

Event=collections.namedtuple('Event', ('start', 'end'))

Endpoint=collections.namedtuple('Endpoint', ('time', 'is_start'))

def add_interval(disjoint_intervals, new_interval):
	
	i, result= 0,  []

	#Processing first stage
	while( i< len(disjoint_intervals) and new_interval.start > disjoint_intervals[i].end):
		result.append(disjoint_intervals[i])
		e=disjoint_intervals[i]
		i+=1
		

	#Processing second stage : overlapped ones
	while( i<len(disjoint_intervals) and new_interval.start <= disjoint_intervals[i].end and new_interval.end>= disjoint_intervals[i].start):
		#new_interval.start=min(disjoint_intervals[i].start, new_interval.start)
		#new_interval.end=max(disjoint_intervals[i].end, new_interval.end)
		new_interval=Event( min(disjoint_intervals[i].start, new_interval.start) ,max(disjoint_intervals[i].end, new_interval.end))
		i+=1

	result.append(new_interval)

	#Processing third stage
	while( i<len(disjoint_intervals) ):
		result.append(disjoint_intervals[i])
		i+=1

	return result

A=[ Event(Endpoint(-4.0, True) , Endpoint(-1.0, False)), Event(Endpoint(0.0, True), Endpoint(2.0, False)),Event(Endpoint(3.0,True),Endpoint(6.0,False)), Event(Endpoint(7.0, True),Endpoint(9.0,False)),Event(Endpoint(11.0, True),Endpoint(12.0,False)), Event(Endpoint(14.0,True),Endpoint(17.0,False))]
for e in add_interval(A,Event(Endpoint(1.0,True), Endpoint(8.0, False) ) ):
	print ''+str(e.start.time )+ ' ' + str(e.end.time)