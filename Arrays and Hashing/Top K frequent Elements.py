def topKFrequent(nums, k):
# Create a dictionary that counts occurence of numbers in array
# Create an array that will keep k most frequent elements
# Each time a dictionary value is assigned check occurence and compare
    occur = {}
    frequent = []

    for num in nums:
        occur[num] = occur.get(num, 0) + 1  # Register occurence 
        if len(frequent) < k and num not in frequent: # If frequent doesn't have enough numbers add numbers to it
            frequent.append(num) # Add number to it
        elif len(frequent) == k: # Else if length == k
            for i in frequent: # For each frequent element
                if occur[i] < occur[num]: # If occurences of array element is less than current element
                    frequent.pop(i) # Remove less element from array
                    frequent.append(num) # Add mode occured element
            
    return frequent