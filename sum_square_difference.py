#
# Calculate the difference between the sum of the squares and square of the sum
#
# @author cigol
#

from math import pow


def sum_of_square(x):
    i = 1
    value = 0
    while (i <= x):
        value += pow(i, 2)
        i += 1
    return value


def square_of_sum(x):
    total = sum(range(1, x+1))
    return pow(total, 2)


def main():
    x = 100
    sum_of_square_val = sum_of_square(x)
    square_of_sum_val = square_of_sum(x)
    print 'Sum of Squares = ', sum_of_square_val
    print 'Square of Sum = ', square_of_sum_val
    difference = square_of_sum_val - sum_of_square_val
    print 'Difference between the sum of the squares and square of the sum = ', difference


main()
