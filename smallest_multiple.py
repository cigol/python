#
# Calculate the smallest multiple in range (1,20)
#
# @author cigol
#
from fractions import gcd


def lcm(x, y):
    val = (x * y) / gcd(x, y)
    return val


def main():
    x = 1
    for num in range(1, 21):
        x = lcm(x, num)
    print 'Smallest common multiple is: ', x

main()

