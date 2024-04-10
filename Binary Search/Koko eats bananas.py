import math
def minEatingSpeed(self, piles, h):
    # n - number of piles
    # n[i] - number of bananas in pile
    # h - hours in which guards will come back
    # k - speed of eating bananas
    # If the pile less than k bananas it still takes one hour to eat them
    # Return k - which is minimum time in which Koko will eat
    # ALL of bananas before guards come back
    l, r = 1, max(piles) # Initialize left and right pointers
    res = r # Result will be equal to right pointer

    while l <= r: # While left pointer less or equal right
        k = (l + r) // 2 # Speed is the middle of l and r pointers

        totalTime = 0 # Total time that it takes to eat
        for p in piles: # For each pile
            totalTime += math.ceil(float(p) / k) # Time it takes to eat bananas is equal
            # to rounded up pile divided by speed
        # Next, we use binary search to tune pointers
        if totalTime <= h: # If time spent less than hours
            res = k # Result is speed
            r = k - 1 # Move right pointer to middle
        else:
            l = k + 1 # Move left pointer to middle
    return res # Return result




        