#!/usr/bin/env python
from __future__ import print_function
from pairing import pair, depair
import timeit
import random


def test_pair(a, b):
    assert depair(pair(a, b)) == (a, b)
    return pair(a, b)


def run_tests(num_random_tests = 0):
    test_pair(22, 33)
    test_pair(2**8, 2**8)
    test_pair(2**16, 2**16)
    test_pair(2**52, 2**52)
    test_pair(2**52, 1)
    test_pair(2**52, 2)
    test_pair(2**52, 55555555)
    for i in range(0, num_random_tests):
        test_pair(random.getrandbits(512), random.getrandbits(512))
        test_pair(random.getrandbits(512), 0)
        test_pair(0, random.getrandbits(512))
        test_pair(random.getrandbits(512), 1)
        test_pair(1, random.getrandbits(512))
    
    try:
        test_pair(-1, -1)
    except ValueError:
        pass  # negative values not supported

    return "Tests pass."


if __name__ == '__main__':
    print(run_tests(2000))

    print("Benchmarking...")
    i = 20000
    print(round(timeit.timeit(run_tests, number=i), 5), "sec,", i, "iterations")
