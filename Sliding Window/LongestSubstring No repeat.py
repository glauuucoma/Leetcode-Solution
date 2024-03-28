def lengthOfLongestSubstring(self, s):
    # Use sliding window technique as well as set

    l = 0 # Initialize left pointer
    subSet = set() # Initialize set cause we are using unique values
    subLen = 0 # Track max len of set
    for r in range(len(s)): # For each character
        while s[r] in subSet: # If right chat in unique subset them
            subSet.remove(s[l]) # Remove left char
            l += 1 # Move left pointer
        subSet.add(s[r]) # If not, add right character to subset
        subLen = max(subLen, r - l+1) # Sublen = Compare existing value of subset with current length
    
    return subLen # Return max length
