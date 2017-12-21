import itertools
import functools
import string

def int_to_string(x):

	is_negative=False
	
	if x<0:
		x, is_negative= -x, True

	s=[]

	while True:
		s.append( chr(ord('0')+x%10) )
		x//=10
		if x==0:
			break

	return ('-' if is_negative else '')+''.join(reversed(s))


print int_to_string(-535)

def string_to_int(x):
	is_positive=1
	start_index=0

	if x[0]=='-':
		is_positive,start_index=-1,1

	number=0
	for s in itertools.islice(x, start_index, None):
		number=number*10+ord(s)-ord('0')

	return number*is_positive

print string_to_int('-535')


def string_to_int_solution(s):
	return functools.reduce(lambda running_sum, c: running_sum *10 + string.digits.index(c), s[s[0]=='-':],0)*(-1 if s[0] =='-' else 1)

print string_to_int_solution('-535')

