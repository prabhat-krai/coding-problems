"""Given a sorted list of words, find the longest compound word in the 
list that is constructed by concatenating the words in the list"""

import collections

class Node:
    def __init__(self, letter = None, isTerminal = False):
        self.letter = letter
        self.children = {}
        self.isTerminal = isTerminal

class Trie:
    def __init__(self):
        self.root = Node('')
    
    def __repr__(self):
        self.output([self.root])
        return ''

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node(letter)
            current.current.children[letter]
        current.isTerminal = True

    def getAllPrefixesofWord(self, word):
        prefix = ''
        prefixes = []
        current = self.root
        for letter in word:
            if letter not in current.children:
                return prefixes
            current = current.children[letter]
            prefix += letter
            if current.isTerminal:
                prefixes.append(prefix)
        return prefixes


    def __contains__(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            else:
                current = current.children[letter]
        return current.isTerminal

    def output(self, currentPath, indent=''):
        currentNode=currentPath[-1]
        if currentNode.isTerminal:
            word=''.join([node.letter for node in currentPath])
            print indent+word
            indent+='  '
        for letter, node in sorted(currentNode.children.items()):
            self.output(currentPath[:]+[node], indent)





def longestWord(words):
    trie = Trie()
    queue = collections.deque()
    for word in words:
        prefixes = trie.getAllPrefixesofWord(word)
        for prefix in prefixes:
            queue.append((word, word[len(prefix):]))
        trie.insert(word)

    longestWord =''
    maxLength = 0
    while queue:
        word, suffix = queue.popleft()
        if suffix in trie and len(word) > maxLength:

