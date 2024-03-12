from collections import defaultdict

def groupAnagrams(strs):
    # Create a defaultdict with default value as an empty list
    res = defaultdict(list)

    # Iterate through each word in array
    for word in strs:

        # For each word create an array with 26 zero's, each zero represents letter
        count = [0] * 26 # a ... z

        # For each character in specific word
        for char in word:
            # Determine what index it is, from 0 to 25th and add occurrence
            count[ord(char) - ord("a")] += 1
        
        # In result dictionary append word to the key, key is just array which represent occurrence of each letter
        res[tuple(count)].append(word)
        # If you don't turn the count list into a tuple and attempt to use 
        # it directly as a key in the dictionary res, you'll encounter a TypeError 
        # because lists are not hashable and cannot be used as dictionary keys in Python.
        

    return res.values()

# In Python, defaultdict(list) is a specialized dictionary-like container 
# provided by the collections module. It's a subclass of the built-in dict 
# type that automatically creates new entries with a default value of an empty 
# list if a key is accessed for the first time.

print(groupAnagrams(["bat", "tap", "tab"]))