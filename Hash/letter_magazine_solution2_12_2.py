import collections

def is_letter_constructible_from_magazine(letter, magazine):
	char_freq_letter=collections.Counter(letter)

	for c in magazine:
		if c in char_freq_letter:
			char_freq_letter[c]-=1
			if char_freq_letter[c]==0:
				del char_freq_letter[c]
				if not char_freq_letter:
					return True
	
	return not char_freq_letter

if __name__ == '__main__':
	print is_letter_constructible_from_magazine("abcde", "abcefghijk")