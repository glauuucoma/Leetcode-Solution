def addBinary(a,b):
	res = ""
	carry = 0

	a,b = a[::-1], b[::-1]

	for i in range(max(len(a), len(b))):
		digitA = a[i] if i < len(a) else