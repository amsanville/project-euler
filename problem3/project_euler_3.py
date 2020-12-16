import math
'''
Find Factor by attempting to divide n by possible factors and recursively finding the factors of those numbers.

Note, algorithm appends the prime factors onto the end of the list provided
'''
def findFactor(n, listFactors):
    prime = True
    # Check if divisible by 2 or 3
    if(n % 2 == 0):
        # Add 2 to the list and try to factor remaining part
        listFactors.append(2)
        findFactor(n / 2, listFactors)
        prime = False
    elif(n % 3 == 0):
        # Add 3 to the list and try to factor remaining part
        listFactors.append(3)
        findFactor(n / 3, listFactors)
        prime = False
    else:
        # Check numbers of the form 6n - 1 and 6n + 1 starting at 5 and 7
        stopVal = math.sqrt(n)
        lower = 5
        upper = 7
        while(lower < stopVal and prime):
            # Check the lower value
            if(n % lower == 0):
                # Add lower to the list and try to factor remaining part
                listFactors.append(lower)
                findFactor(n / lower, listFactors)
                prime = False
            # Check the upper value only if still prime
            if(n % upper == 0 and prime):
                # Add upper to the list and try to factor remaining part
                listFactors.append(upper)
                findFactor(n / upper, listFactors)
                prime = False
            # Update
            lower += 6
            upper += 6

    # If n was prime, add it to the list
    if(prime):
        listFactors.append(n)

'''
Some tests as well as solving the problem of interest
'''
def main():
    # n = 1105 = 5*13*17
    n1 = 1105
    list1 = []
    findFactor(n1, list1)
    print(list1)

    # n = 600,851,475,143
    n2 = 600851475143
    list2 = []
    findFactor(n2, list2)
    print(list2)

if __name__ == '__main__':
    main()