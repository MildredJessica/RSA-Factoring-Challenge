#!usr/bin/python3


def product(n):
    """Factorize as many numbers as possible
    into a product of two smaller numbers.
    """
    if n % 2 == 0:
        print("{}={:d}*{}".format(n, int(n/2), 2))
        return
    for num in range(3, n, 2):
        if ((n % num) == 0):
            print("{}={}*{}".format(n, int(n/num), num))
            return
