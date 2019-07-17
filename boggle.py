def boggleBoard(board, words):
    check_words = {}
    for word in words:
        check_words[word] = True
    if word in check_words:
        print("Works")
    
boggleBoard([], ["Pranav", "Prabhat"])