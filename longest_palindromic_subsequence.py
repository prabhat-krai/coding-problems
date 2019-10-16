"""
Number of elements in the subsequence of longest plaindrome.
"""


seq = input()
n = len(seq)

dp = [[None]*n for _ in range(n)] 

for i in range(n): # a char forms a single char palindrome
    dp[i][i] = 1

def find_subsequence(i,j): 
    if(i == j):
        return 1
    if(seq[i] == seq[j]):
        if(i + 1 == j):
            return 2
        else:
            return 2 + find_subsequence(i + 1, j - 1)
    else:
        return max(find_subsequence(i + 1, j), find_subsequence(i, j - 1))


def find_subsequence_dp(i, j): #Using Memoization to avoid repeat calls
    if(dp[i][j] is None):
        if(seq[i] == seq[j]):
            if(i + 1 == j):
                dp[i][j] = 2
                return dp[i][j]
            else:
                dp[i][j] = 2 + find_subsequence(i + 1, j - 1)
        else:
            dp[i][j] = max(find_subsequence(i + 1, j), find_subsequence(i, j - 1))
            return dp[i][j]
    else:
        return dp[i][j]
    return dp[0][n-1]

print(find_subsequence(0, n - 1))
print(find_subsequence_dp(0, n - 1))
