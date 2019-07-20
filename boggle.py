def boggleBoard(board, words):
    check_words = {}
    for word in words:
        check_words[word] = True
    
    x = 0
    y = 0
    currWord = board[x][y]
    findWords(currWord, board, check_words, x+1, y)
    findWords(currWord, board, check_words, x-1, y)
    findWords(currWord, board, check_words, x, y+1)
    findWords(currWord, board, check_words, x+1, y-1)
    findWords(currWord, board, check_words, x+1, y+1)
    findWords(currWord, board, check_words, x+1, y-1)
    findWords(currWord, board, check_words, x-1, y+1)
    findWords(currWord, board, check_words, x-1, y-1)


def findWords(word, board, words, x, y):
    