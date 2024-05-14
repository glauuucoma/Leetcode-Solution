# Time complexity - O(2^t), where t is the target
def combinationSum(candidates, target):
    res = []
    # cur - current combination
    # i - index
    # total - sum of elements included in cur

    def dfs(i, cur, total):
        if total == target: # Base case
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target: # Base case 2
            return
        
        # Do Include value, candidate
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])

        # Not include value
        cur.pop()
        dfs(i+1, cur, total)
    
    dfs(0, [], 0)
    return res