def boggleBoard(board, words):
    trie = Trie()
    check_words = {}
    for word in words:
        check_words[word] = True
    



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
