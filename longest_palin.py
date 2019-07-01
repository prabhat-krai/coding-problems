def longest_palindrome(text):
    end_points = [0,1]
    for i in range(1, len(text)):
        palin_odd = findPalindrome(text,i-1, i+1)
        palin_even = findPalindrome(text, i-1, i)
        longest = max(palin_even, palin_odd, key = lambda x: x[1] - x[0])
        end_points = max(longest, end_points, key = lambda x: x[1] - x[0])

    return text[end_points[0]: end_points[1]]

def findPalindrome(string, i, j):
    while (i >= 0 and j < len(string)):
        if(string[i] != string[j]):
            break 
        i -= 1
        j += 1
    
    return [i+1, j]

print(longest_palindrome("bbloooojoooolcc"))


