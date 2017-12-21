def is_palindromic(s):
	return all( s[i] ==s[~i] for i in range(len(s)))

print is_palindromic('12321')
print is_palindromic('1232')