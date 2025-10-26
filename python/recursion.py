def degree(n, d):
	if d < 2:
		return n
	return n * degree(n, d - 1)

def sum_digit(n):
	if n < 10:
		return n
	return (n % 10) + sum_digit(int(n / 10))

def is_palindrom(s):
	if len(s) < 2:
		return True
	if s[0] != s[-1]:
		return False
	return is_palindrom(s[1:-1])