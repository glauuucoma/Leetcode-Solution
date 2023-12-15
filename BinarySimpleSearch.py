sampleArr = [1,3,5,6,7,5,4,3,4,5]

def binarySearch(array, element):
	low = 0
	high = len(sampleArr) - 1

	while low>=high:
		mid = high/2
		if sampleArr[mid] == element:
			return element
			