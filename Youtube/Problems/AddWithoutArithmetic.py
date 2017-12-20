

def addWithoutArithmetic(i, j):

    while j != 0:

        # common bits b/w i and j
        carry = i & j

        # sum of bit where 1 is not set (XOR)
        i = i ^ j

        # shift carry by 1
        j = carry << 1

    return i


print(addWithoutArithmetic(10, 20))
