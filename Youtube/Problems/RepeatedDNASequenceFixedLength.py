

class trienode(object):

    def __init__(self, c):
        self.char = c
        self.children = {}			# maps a character value to a trienode representing this character
        self.end = 0				# a flag indicating the number of times this node has been the end of a string

    def __repr__(self):
        return str(self.char)


class trie(object):

    def __init__(self):

        self.root = trienode(None)


    def addWord(self, word):
        cur = self.root

        for character in word:
            if not (character in cur.children):
                cur.children[character] = trienode(character)

            cur = cur.children[character]

        cur.end += 1

    def _countRepeated(self, currentString, curNode, repeated):
        if curNode.end > 1:
            repeated.append(currentString)
            return

        if curNode.end == 0:
            for child in curNode.children:
                self._countRepeated(currentString + child, curNode.children[child], repeated)

    def countRepeated(self):
        repeated = []
        for child in self.root.children:
            self._countRepeated(child, self.root.children[child], repeated)

        return repeated


class Solution:

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        trieStruct = trie()
        i = 0
        while len(s) - i > 9:
            trieStruct.addWord(s[i: i +10])
            i += 1
        return trieStruct.countRepeated()

    def simplerFindRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        rep = set()
        seen = set()

        i = 0
        while len(s) - i > 9:
            w = s[i:i + 10]
            if w in seen:
                rep.add(w)
            else:
                seen.add(w)
            i += 1

        return list(rep)