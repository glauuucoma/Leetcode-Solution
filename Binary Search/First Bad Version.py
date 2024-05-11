def isBadVersion(): # Dummy substitute
    pass

def firstBadVersion(self, n):
    # We can solve this problem using Binary search
    low = 1 # Left pointer
    high = n # Right pointer
    mid = 0 # Middle
    result = n # Bad version will always be in the end

    while(low<=high):
        mid = (high+low)//2 # calculate mid pointer
        if isBadVersion(mid): # if v. is bad
            result = mid # record value as the lowest bad version
            high = mid-1 # update pointer to travrse thru left part
        else: # Value is not bad
            low = mid + 1 # update pointer to travrse thru right part
    return result # return lowest bad version