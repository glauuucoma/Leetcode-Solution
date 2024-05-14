def subsets(self, nums):
        res = [] # Result, all subsets together
        subset = [] # Current subset

        def dfs(i): # recursive function
            if i >= len(nums): # Base case to add subset to results
                res.append(subset[:]) # Add copy of curr subset to result array 
                return # Exit current function call

            # decision to include nums[i]
            subset.append(nums[i]) # Append number to current subset
            dfs(i + 1) # Move up to other number

            # decision not to include nums[i]
            subset.pop() # Remove last element
            dfs(i + 1) # # Move up to other number
        
        dfs(0) # Call helper function on first element of array
        return res # Return result array with all the subsets