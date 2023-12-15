from collections import defaultdict

def groupAnagrams(strs):

	res = defaultdict(list) # Create dictionary that would not throw Error

	for s in strs: # For each word in array

		count = [0] * 26 # Create array of 26 zero's

		for c in s: # For each letter in word
			count[ord(c) - ord("a")] += 1 # Increment 

		res[tuple(count)].append(s) # Create dict. key that uses array turned into tuple and append initial word to it

	return res.values()

groupAnagrams(["eat","tea","tan","ate","nat","bat"])