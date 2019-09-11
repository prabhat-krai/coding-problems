hashTable = ["", "", "abc", "def", "ghi", "jkl",  
                    "mno", "pqrs", "tuv", "wxyz"] 
   
def printWordsUtil(input_keypad, curr, output, n): 
    if(curr == n): 
        print(output) 
        return
           
    for i in range(len(hashTable[input_keypad[curr]])): 
        output.append(hashTable[input_keypad[curr]][i]) 
        printWordsUtil(input_keypad, curr + 1, output, n) 
        output.pop() 
        if(input_keypad[curr] == 0 or input_keypad[curr] == 1): 
            return;  
               
def printWords(input_keypad, n): 
    printWordsUtil(input_keypad, 0, [], n) 
      


input_keypad = [5, 6, 2] 
n = len(input_keypad) 
printWords(input_keypad, n)