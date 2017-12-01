
class TrieNode(object):
    """
    The trie node which stores a dictionary of edges (an adjacency list),
    and whether the node represents the end of a word and the number of words using this prefix.
    """

    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.prefixes = 0

    def getChildren(self):
        return self.children

    def getEndOfWord(self):
        return self.endOfWord

    def isEnd(self):
        self.endOfWord = True

    def incrementPrefix(self):
        self.prefixes += 1

    def getPrefixes(self):
        return self.prefixes


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, w):
        """
        Adds the words to the trie starting at the root,
        builds new trie nodes if required.
        """
        cur = self.root

        # For each letter in the word
        for i in w:

            # Look at current position if we can go to the next letter
            if i in cur.getChildren():

                # If so then get that as the next letter
                cur = cur.getChildren()[i]
                cur.incrementPrefix()

            # Otherwise create a new trie node representing the jump to the next value
            else:
                temp = TrieNode()
                temp.incrementPrefix()
                # cur.incrementPrefix()
                cur.getChildren()[i] = temp
                cur = temp

        # When we are finished the last cur is the end of the word so we mark it as such
        cur.isEnd()

    def countWords(self):
        """
        Traverse the trie to see the number of endOfWord flags that are present
        """
        words = 0

        # Go through each of the children to traverse the trie
        for i in self.root.getChildren():
            words += self._recursiveTraverseWords(self.root.getChildren()[i])

        return words

    def _recursiveTraverseWords(self, node):
        """
        Recursive tree traversal
        """
        words = 0

        # Check if a word can be made at this node
        if node.getEndOfWord():
            words += 1

        # Go through each of the children to traverse the trie
        for i in node.getChildren():
            words += self._recursiveTraverseWords(node.getChildren()[i])

        return words

    def countPrefix(self, pre):
        """
        Follows the root using the inputted prefix to check if it is present in the trie,
        if so returns the number of times that prefix was used when inputting words
        """
        if pre[0] in self.root.getChildren():
            return self._recursivePrefix(pre, 1, self.root.getChildren()[pre[0]])
        return 0

    def _recursivePrefix(self, pre, i, node):
        """
        Recursive tree traversal
        """
        if i == len(pre):
            return node.getPrefixes()

        if pre[i] in node.getChildren():
            return self._recursivePrefix(pre, i + 1, node.getChildren()[pre[i]])
        return 0

    def search(self, w):
        """
        Follows the root using the inputted word to check if it is present in the trie
        Uses the endOfWord flag to ensure the final word is actually in the dictionary and not just the prefix
        """
        if w[0] in self.root.getChildren():
            return self._recursiveSearch(w, 1, self.root.getChildren()[w[0]])
        return False

    def _recursiveSearch(self, w, i, node):
        """
        Recursive tree traversal
        """
        if i == len(w):
            return node.getEndOfWord()

        if w[i] in node.getChildren():
            return self._recursiveSearch(w, i + 1, node.getChildren()[w[i]])
        return False


def testTrie():
    trie = Trie()

    trie.addWord("hello")
    trie.addWord("he")
    trie.addWord("hell")
    trie.addWord("hellsinki")
    trie.addWord("hellen")
    trie.addWord("the")
    trie.addWord("cat")

    print("0", 7 == trie.countWords())

    print("1", True is trie.search("hello"))
    print("2", True is trie.search("cat"))
    print("3", False is trie.search("hellox"))
    print("4", False is trie.search("hel"))

    print("5", 1 == trie.countPrefix("t"))
    print("6", 1 == trie.countPrefix("th"))
    print("7", 1 == trie.countPrefix("the"))
    print("8", 5 == trie.countPrefix("he"))
    print("9", 4 == trie.countPrefix("hell"))


testTrie()
