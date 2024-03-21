def lengthOfLongestSubstring(s):
    # Use sliding window technique
    charSet = set() # Create set for unique chars
    res = 0 # Max len counter
    l = 0 # Left pointer

    for r in range(len(s)):  # For each letter in string
        while s[r] in charSet: # If s[r] character in set
            charSet.remove(s[l]) # Remove previous characters
            l += 1 # Move left pointer
        charSet.add(s[r]) # Add right pointer to set
        res = max(res, r - l + 1) # Define result by finding out lenfth of string and comparing it with existing

    return res

# adcacvb