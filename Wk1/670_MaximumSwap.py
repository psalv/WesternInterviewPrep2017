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
            for examineDigit in range(len(numArray) - 1, currentDigit, -1):
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
print(Solution.maximumSwap(None, 1993))




