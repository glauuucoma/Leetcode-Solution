def getNthFib(n):
    F0 = 0;
    F1 = 1;
    if n == F0:
        return 0
    elif n == F1:
        return 0
    else:
        fNumbers = [F0, F1]
        currentF = 2
        while len(fNumbers)<n:
            fNumbers.append(fNumbers[currentF-1] + fNumbers[currentF-2])
            currentF += 1
        return fNumbers[n-1]

print(getNthFib(6))