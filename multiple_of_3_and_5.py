#
# Calculate the sum of multiples of 3 and 5 for range (0, 1000)
# Example of range (0, 10) is also given
#
# @author cigol
#

def multiple_of_3(list_arr):
    sum_of_3s = 0

    for n in list_arr:
        if (n % 3 == 0):
            sum_of_3s = sum_of_3s + n

    return sum_of_3s


def multiple_of_5(list_arr):
    sum_of_5s = 0
    for n in list_arr:
        if (n % 5 == 0):
            sum_of_5s = sum_of_5s + n
    return sum_of_5s


def output(list_range):
    val_3s = multiple_of_3(list_range)
    val_5s = multiple_of_5(list_range)
    print "Sum of all multiples of 3 and 5 between 0 and 10 is : ", val_3s + val_5s


def main():
    x = 10
    list_range1 = list(range(0, x))  # list of val from 0 to 10
    output(list_range1)
    y = 1000
    list_range2 = list(range(0, y))  # list of val from 0 to 1000
    output(list_range2)


main()
