#
# Calculate sum of all even numbers of a Fibonacci sequence
#
# @author cigol
#

def main():
    x, y = 0, 1
    index = 0
    fib_list = []
    total = 0
    while True:
        x, y = y, x + y
        fib_list.append(y)
        if (y > 4000000):  # manual limit of 4,000,000 is set my problem statement
            break
    print 'List: ', fib_list
    for num in fib_list:
        if (num % 2 == 0):
            total = total + num
    print 'Sum of all even fibonacci numbers = ', total


main()
