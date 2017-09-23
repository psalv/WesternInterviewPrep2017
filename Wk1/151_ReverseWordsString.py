class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        reversedString = ''
        for i in range(len(words) - 1, -1, -1):
            if reversedString is not '':
                reversedString += " "
            reversedString += words[i]
        return reversedString


print(Solution.reverseWords(Solution(), "this is a test"))
print(Solution.reverseWords(Solution(), "this is a much much longer test case because It has Many More words"))

