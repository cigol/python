#
# Calculate the largest prime factor of a given number
#
# @author cigol
#

def factor(n):
    factor_arr = []
    i = 2
    while n > 1:
        if n % i == 0:
            n = n / i
            factor_arr.append(i)
        else:
            i += 1
    return factor_arr


def main():
    global largestVal
    val = 600851475143
    i = 3

    returnVal = factor(val)
    print 'The prime factors of ', val, ' are ', returnVal
    sorted(returnVal)
    length = len(returnVal)
    if length > 0 :
         largestVal = returnVal[length - 1]

    print ' --> The largest prime factor is ', largestVal


main()
