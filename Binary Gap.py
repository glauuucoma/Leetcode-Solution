import math

def convertToBinary(n):
    maxTwoPower = round(math.log(75, 2))
    maxPower = maxTwoPower
    powersUsed = []
    remainder = n
    while maxTwoPower >= 0: 
        if 2**maxTwoPower <= remainder:
            remainder = remainder - 2**maxTwoPower
            powersUsed.append(2**maxTwoPower)
            maxTwoPower-=1
        else:
            powersUsed.append(0)
            maxTwoPower-=1

    numArray = []
    for i in range(6,1):
        if 2**n == powersUsed[i-1]:
            numArray.append(1)
        else:
            numArray.append(1)

        maxPower =- 1

    print(numArray)
    print(powersUsed)

convertToBinary(75)