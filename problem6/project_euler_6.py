import matplotlib.pyplot as plt

'''
Calculates the sum requested, i.e. the difference between the square of the sum of the first n natural numbers and the sum of the squares of the first n natural numbers
'''
def calcSum(n):
    sum = 0
    sumSqrs = 0
    for i in range(1, n + 1):
        sum += i
        sumSqrs += i**2
    return sum**2 - sumSqrs

'''
Constructs plot of values of n versus the values of the sum
'''
def plotVals():
    plot_x = [1, 2, 3, 4, 5, 6, 7]
    plot_y = [1, 5, 14, 30, 55, 91, 140]

    # Make the plot
    fig, ax = plt.subplots()
    ax.plot(plot_x, plot_y)
    ax.set_xlabel('n')
    ax.set_ylabel('S')
    ax.set_title('Value of sum')
    plt.show()

def main():
    print(calcSum(100))
    plotVals()

if __name__ == "__main__":
    main()
