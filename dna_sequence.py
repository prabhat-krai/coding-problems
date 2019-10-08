map_of_substrings = {}

dna_sequence = input()
repeating_dna = []
for i in range(len(dna_sequence) - 10):
    dna_substring = dna_sequence[i:i+10]
    if(dna_substring in map_of_substrings):
        map_of_substrings[dna_substring] += 1
    else:
        map_of_substrings[dna_substring] = 1

for key in map_of_substrings:
    if(map_of_substrings[key] > 1):
        repeating_dna.append(key)

print(repeating_dna)