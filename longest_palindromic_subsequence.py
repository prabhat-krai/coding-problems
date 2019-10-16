seq = input()
seq = list(seq)

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

print(find_subsequence(0, len(seq) - 1))