

import math


def getNum(n):
    return 2*n + 3


def removeCur(sieve, cur):
    c = getNum(cur)
    for i in range(cur + 1, len(sieve)):
        if getNum(i) % c == 0:
            sieve[i] = False


def generateSieve(n):
    sieve = []
    for i in range(n//2):
        sieve.append(True)

    cur = 0
    while getNum(cur) <= math.sqrt(n):
        removeCur(sieve, cur)

        cur += 1
        while cur < len(sieve) and not sieve[cur]:
            cur += 1

    return sieve


def printPrimes(n):
    sieve = generateSieve(n)
    for i in range(len(sieve)):
        if sieve[i]:
            print(getNum(i))


printPrimes(10000)
