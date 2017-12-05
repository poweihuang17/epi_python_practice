import collections

def is_letter_constructible_from_magazine(letter, magazine):
	return (not collections.Counter(letter)-collections.Counter(magazine))

if __name__ == '__main__':
	print is_letter_constructible_from_magazine("abcde", "abcdefghijk")