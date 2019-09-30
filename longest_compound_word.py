"""Given a sorted list of words, find the longest compound word in the 
list that is constructed by concatenating the words in the list"""

class Node:
    def __init__(self, letter = None, isTerminal = False):
        self.letter = letter
        self.children = {}
        self.isTerminal = isTerminal

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

        
        