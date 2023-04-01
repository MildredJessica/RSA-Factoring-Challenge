#!/usr/bin/python3
import sys
from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp
func = __import__('factor_func').product


def unix_time(function):
    '''Return `real`, `sys` and `user` elapsed time, like UNIX's command `time`
    You can calculate the amount of used CPU-time used by your
    function/callable by summing `user` and `sys`. `real` is just like the wall
    clock.
    Note that `sys` and `user`'s resolutions are limited by the resolution of
    the operating system's software clock (check `man 7 time` for more
    details).
    '''
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    function()
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()

    return "\nreal: {}\nuser: {}\nsys: {}".format(
        end_time - start_time,
        end_resources.ru_utime - start_resources.ru_utime,
        end_resources.ru_stime - start_resources.ru_stime)


def factors():
    """Reads a file to print out all the factors of a number"""
    with open(sys.argv[1], 'r') as prime:
        print("Open")
        line = prime.readline()
        while line != '':
            n = int(line)
            func(n)
            line = prime.readline()


def main():
    print(unix_time(factors))

if __name__ == "__main__":
    main()
