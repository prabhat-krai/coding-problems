def levenshteinDistance(str_1, str_2):
    changes = [[x for x in range(len(str_1) + 1)]for y in range(len(str_2) + 1)]
    for i in range(1, len(str_2)+1):
        changes[i][0] = changes[i-1][0] + 1

    for r in range(1, len(str_2) + 1):
        for c in range(1, len(str_1) + 1):

            if(str_1[c - 1] == str_2[r - 1]):
                changes[r][c] = changes[r - 1][c - 1]
            else:
                changes[r][c] = min(changes[r - 1][c - 1], changes[r - 1][c], changes[r][c - 1]) + 1   

    return changes[-1][-1]

print(levenshteinDistance("Bangalore", "Bengaluru"))
print(levenshteinDistance("India", "Bharat"))
print(levenshteinDistance("Python", "Pythonic"))
print(levenshteinDistance("Flask", "Spring"))

