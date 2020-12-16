class LargeInteger:
    ''' Large Integer

    Creates a representation for integers or arbitrary size. Sign is stored at the zeroth index as either a +1 or -1
    '''
    # digitList - List of integers holding all the digits, ones place is last
    digitList

    def __init__(self):
        ''' Blank Constructor

        Creates a LargeInteger that stores 0
        '''

        # Empty constructor, assume 0:
        digitList = [1, 0]

    def __init__(self, n):
        ''' Constructor from an integer

        Creates a LargeInteger based on an integer input
        '''
        # Deal with the sign of the integer n
        isNegative = False
        if(n < 0):
            isNegative = True
            n *= -1

        # Cast integer to a string and put each digit into the list
        intText = str(n)
        sizeInt = len(intText)
        
        # Initialize
        digitList = [0] * sizeInt + 1
        # Get the sign
        if(isNegative):
            digitList[0] = -1
        else:
            digitList[0] = 1
        # Get the remaining digits
        for i in range(0, sizeInt):
            digitList[i + 1] = int(intText[i])

    def add(self, otherLargeInteger):
        ''' Add

        Adds the two LargeIntegers together. Determines behavior based on the signs of the integers.
        otherLargeInteger - the other LargeInteger to be subtracted
        '''

        # Check data type and convert any ints to LargeIntegers
        if(isinstance(otherLargeInteger, int)):
            otherLargeInteger = LargeInteger(otherLargeInteger)
        
        # Reorganize into a shorter and longer number in terms of digits
        if(len(self.digitList) > len(otherLargeInteger.digitList)):
            largeNum = self.digitList
            smallNum = otherLargeInteger.digitList
        else:
            smallNum = self.digitList
            largeNum = otherLargeInteger.digitList

        # Calculate the stopping point
        stop = len(smallNum)
        if(len(smallNum) == len(largeNum)):
            sameLength = True
            stop -= 1

        # Initialize the output
        temp = [0] * len(largeNum)

        # Calculate all digits until at least one number runs out of digits
        for i in range(1, stop):
            # Calculate the digit
            temp[-i] += (self.digitList[0] * self.digitList[-i] + otherLargeInteger.digitList[0] * otherLargeInteger.digitList[-i])
            # Correct if larger than 10
            while(temp[-i] >= 10):
                temp[-i] -= 10
                temp[-i - 1] += 1

        if(sameLength):

        else:
            for i in range(stop + 1, len(largeNum)):
                temp[-i] = largeNum
        # Return the result
        return temp

    def subtract(self, otherLargeInteger):
        ''' Subtract

        Subtracts the other LargeInteger from this LargeInteger by using the add method and a sign change.
        otherLargeInteger - the other LargeInteger to be subtracted
        '''
        return digitList

    def multiply(self, otherLargeInteger):
        # TODO!
        return digitList

    def divide(self, otherLargeInteger):
        # TODO!
        return digitList


def findLargestProduct(numberList, n):
    ''' Find Largest Sum

    Finds the largest product of n adjacent digits in the number provided.
    numberList - a list of the digits of the number of interest
    n - the number of adjacent digits to take the product of
    '''
    k = len(numberList)
    if(k < n):
        # Insufficient numbers in the list of numbers
        return 0
    else:
        # Allocate space
        product = [-1] * k
        for i in range(0, k - n + n // 2):
            # Initialize product
            product[i] = 1

            # Start a second index for calculating the product
            index = i - n // 2
            counter = 0
            while(counter < n):
                product[i] *= numberList[index]
                index += 1
                counter += 1

        # Find the max and it's location
        maxVal = max(product)
        maxIndex = product.index(maxVal)

        # Print
        print('The maximum value: ', maxVal)
        print('The sequential digits: ', numberList[maxIndex - n // 2:maxIndex - n // 2 + n])

def loadLargeNumber(file):
    ''' Load Large Number

    Loads a number that is to large to be represented by an it from the given file.
    file - the name of the file to load the number from, assumes the file is only digits
    return - a list of all the digits from largest to ones place
    '''

    # Load the file as a string
    numText = open(file).read()

    # Process each digit character into an integer
    n = len(numText)
    numList = [0] * n
    for i in range(0, n):
        numList[i] = int(numText[i])

    # Return the result
    return numList

def main():
    # Create the digit string file for the problem
    digitStr = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    open('project_euler_8_num.txt', 'w+').write(digitStr)

    # Load the data
    numberList = loadLargeNumber('project_euler_8_num.txt')
    # Example problem
    findLargestProduct(numberList, 4)
    # Problem to solve
    findLargestProduct(numberList, 13)

if __name__ =='__main__':
    main()