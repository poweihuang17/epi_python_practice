import collections
def can_string_be_a_palindrome(s):
	return sum(v%2 for v in collections.Counter(s).values())<=1

if __name__ == '__main__':
	print can_string_be_a_palindrome("abdba")
	print can_string_be_a_palindrome("abcde")