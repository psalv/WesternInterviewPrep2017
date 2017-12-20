import random


def rand6():
    return random.randint(0, 5)


def rand7():
    print(rand6())
    print(rand6())


rand7()