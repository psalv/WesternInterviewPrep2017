class Solution(object):

    # Can use a max heap to store the values, but there really aren't that many digits
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        largest = -1
        largestIndex = -1
        strRepresentation = str(num)
        for i in range(0, len(strRepresentation)):
            if int(strRepresentation[i]) > largest:
                largest = int(strRepresentation[i])
                largestIndex = i

