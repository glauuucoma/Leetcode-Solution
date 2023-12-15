def isValid(s):
	if len(s) == 0 or len(s) % 2 != 0:
		return False

	charactersValid = {'(': ')', '{': '}', '[': ']'}
	for i in range(0,len(s)):
		if s[i] in charactersValid and s[i+1] == :
			return False
		else:
			i += 1

	return True

print(isValid("()"))
print(isValid("()[]"))
print(isValid("()["))
print(isValid("()[]{}"))