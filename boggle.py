"""
A 2D array is given and a list of words. 
Write a program that returns all the words contained in the boggle board.
"""


def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for letter in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())



















class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol =  "*"
    
    def add_word(self, word):
        current  = self.root 
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = word
