# Explanation
# There is minimal integer values that changes as we iterate thru array
# and int temp value that represents current value

# Time and Space complexity
# Time: O(n^2)
# Space O(1)

def selectionSort(lst):
    for i in range(len(lst)):
        min_num = i
        for j in range(i+1, len(lst)):
            if lst[min_num] > lst[j]:
                min_num = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_num] = lst[min_num], lst[i]

    return lst


print(selectionSort([4,5,3,2,5,6,4,3,2]))


