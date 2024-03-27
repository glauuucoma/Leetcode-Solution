def productExceptSelf(self, nums):    
    # Res array init one number for each value 
    # Prefix/Postfix = 1
    # To break down each loop
    # From begining or end for i
    # Result for i equals to prefix or multiplied by postfix
    # Prefix/Postfix equals multiplued by nums[i]
    # Return res

    res = [1] * len(nums) # Creating array with one value for each element of nums

    prefix = 1 # Initialize prefix base value
    for i in range(len(nums)): # For each value from beginning
        res[i] = prefix # Element at i index equals to prefix
        prefix *= nums[i] # Prefix equals to prefix multiplied by number
    postfix = 1 # Do the same with postfix, init base value
    for i in range(len(nums) - 1, -1, -1): # Start from end
        res[i] *= postfix # Element at i index equals to elemt multiplied by postifx
        postfix *= nums[i] # Postfix equals postfix multiplied by nums[i]

    return res