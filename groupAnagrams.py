# How the solution works??

# At first we import defaultdict from collections, so dictionary will have default value that is empty array (list)
# Create dictionary res (result)
# Iterate thru each word in array
# Create count of letter for each word, array filled with 26 zeros
# Iterate thru each letter in word
# For each letter index increment if occurs
# After the loop of letter in the end of loop of word 
# Create dict key that consists of array turned into tuple and add value which is word
# In the end return values of dict

from collections import defaultdict

def groupAnagram(strs):
	res = defaultdict(list)

	for word in strs:

		count = [0] * 26 # a...z

		for letter in word:

			count[ord(letter)-ord("a")] += 1

		res[tuple(count)].append(word)

	return res.values()



print(list(groupAnagram(["eat","tea","tan","ate","nat","bat"])))