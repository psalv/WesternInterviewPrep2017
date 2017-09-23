class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numArray = []
        for i in str(num):
            numArray.append(int(i))

        for currentDigit in range(len(numArray)):
            largest = -1
            largestIndex = -1
            for examineDigit in range(currentDigit + 1, len(numArray)):
                if numArray[currentDigit] < numArray[examineDigit] and largest < numArray[examineDigit]:
                    largest = numArray[examineDigit]
                    largestIndex = examineDigit
            if largest != -1:
                temp = numArray[currentDigit]
                numArray[currentDigit] = largest
                numArray[largestIndex] = temp

                buildNum = ''
                for i in numArray:
                    buildNum += str(i)
                return int(buildNum)

        return num


print(Solution.maximumSwap(None, 129))
print(Solution.maximumSwap(None, 193))
print(Solution.maximumSwap(None, 321))

# TODO ! Deal with case when taking the first isn't necessarily the best
print(Solution.maximumSwap(None, 1993))




