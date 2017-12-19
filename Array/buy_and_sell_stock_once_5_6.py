def buy_and_sell_once(A):
	
	maximum=float('-inf')
	minimum=float('inf')

	value=float('-inf')

	for item in A:
		minimum=min(minimum, item)
		value=max(value, item-minimum)

	return value

print buy_and_sell_once([310, 315, 295, 260,270,290,230,255,250])
